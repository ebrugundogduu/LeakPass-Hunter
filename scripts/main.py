
import frida
import sys
import argparse
import time
from password_detector import PasswordDetector

class LeakPassHunter:
    def __init__(self, target_package, output_file=None, duration=None):
        self.target_package = target_package
        self.output_file = output_file
        self.duration = duration
        self.detector = PasswordDetector()
        self.script = None
        self.process = None

    def _on_message(self, message, data):
        """Frida script'inden gelen mesajları işler."""
        if message['type'] == 'send':
            payload = message['payload']
            if payload['type'] == 'status':
                print(f"[STATUS] {payload['message']}")
            elif payload['type'] == 'log_data':
                log_message = payload['message']
                detected_passwords = self.detector.detect_passwords(log_message)
                if detected_passwords:
                    output = (
                        f"\n[LEAK DETECTED!] "
                        f"Timestamp: {payload['timestamp']}\n"
                        f"Source: {payload['source']}\n"
                        f"Original Log: '{log_message}'\n"
                        f"Detected Passwords/Secrets: {detected_passwords}\n"
                        f"{'-'*50}"
                    )
                    print(output)
                    if self.output_file:
                        with open(self.output_file, 'a', encoding='utf-8') as f:
                            f.write(output + '\n')
        elif message['type'] == 'error':
            print(f"[FRIDA ERROR] {message['description']}")

    def run(self):
        print(f"[*] Connecting to Frida...")
        try:
            device = frida.get_usb_device(timeout=10)
            print(f"[*] Connected to device: {device.name}")
        except Exception as e:
            print(f"[-] Error connecting to device: {e}")
            sys.exit(1)

        try:
            print(f"[*] Attaching to application: {self.target_package}")
            self.process = device.spawn([self.target_package])
            session = device.attach(self.process)
            print(f"[*] Spawning {self.target_package} and attaching...")

            with open('frida_hooks.js', 'r', encoding='utf-8') as f:
                script_code = f.read()

            self.script = session.create_script(script_code)
            self.script.on('message', self._on_message)
            self.script.load()

            device.resume(self.process)
            print("[+] LeakPass Hunter started. Waiting for log data...")
            print("    (Press Ctrl+C to stop the analysis)")

            if self.duration:
                print(f"[*] Analysis will run for {self.duration} seconds.")
                time.sleep(self.duration)
                print("[*] Analysis duration ended.")
            else:
                sys.stdin.read()

        except frida.core.RPCException as e:
            print(f"[-] Frida RPC Error: {e}")
        except FileNotFoundError:
            print("[-] Error: 'frida_hooks.js' not found.")
        except Exception as e:
            print(f"[-] Unexpected error: {e}")
        finally:
            if self.script:
                print("[*] Unloading Frida script...")
                try:
                    self.script.unload()
                except Exception as e:
                    print(f"[-] Error unloading script: {e}")
            if self.process:
                print(f"[*] Killing process {self.target_package}...")
                try:
                    device.kill(self.process)
                except Exception as e:
                    print(f"[-] Error killing process: {e}")
            print("[*] LeakPass Hunter stopped.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="LeakPass Hunter: Detects sensitive data leaks in Android application logs using Frida."
    )
    parser.add_argument('--target_package', type=str, required=True,
                        help='The package name of the Android application to monitor (e.g., com.example.app).')
    parser.add_argument('--output', type=str,
                        help='Optional: File to write detected leaks to. Defaults to console.')
    parser.add_argument('--duration', type=int,
                        help='Optional: Duration (seconds) to run analysis. Defaults to unlimited.')

    args = parser.parse_args()

    hunter = LeakPassHunter(
        target_package=args.target_package,
        output_file=args.output,
        duration=args.duration
    )
    hunter.run()
