# password_detector.py

import re

class PasswordDetector:
    def __init__(self):
        # Parola içerebilecek ifadeleri yakalayacak RegEx desenleri
        self.password_patterns = [
            re.compile(r'(?i)(pass(word)?|şifre|parola|secret|api_key|token)[:=\s]*([a-zA-Z0-9!@#$%^&*()_+=\-{}\[\]|\\:;"\'<,>.?/`~]{6,})'),
            re.compile(r'[A-Za-z0-9+/=]{10,}={0,2}'),  # Base64 benzeri
            re.compile(r'[0-9a-fA-F]{16,}'),           # Hex / hash benzeri
            re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+=\-{}$begin:math:display$$end:math:display$|\\:;"\'<,>.?/`~]).{8,}'),  # Güçlü parola
        ]

        # Yanlış pozitifleri azaltacak kara liste desenleri
        self.blacklist_patterns = [
            re.compile(r'(?i)https?://[^\s]+'),  # URL
            re.compile(r'(?i)file://[^\s]+'),    # Dosya yolu
            re.compile(r'[a-fA-F0-9]{32}'),      # MD5
            re.compile(r'[a-fA-F0-9]{40}'),      # SHA1
            re.compile(r'[a-fA-F0-9]{64}'),      # SHA256
            re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'),  # UUID
        ]

    def _is_blacklisted(self, text: str) -> bool:
        for pattern in self.blacklist_patterns:
            if pattern.search(text):
                return True
        return False

    def detect_passwords(self, log_message: str) -> list:
        found_passwords = []

        if not log_message or self._is_blacklisted(log_message):
            return found_passwords

        for pattern in self.password_patterns:
            matches = pattern.findall(log_message)
            for match in matches:
                if isinstance(match, tuple):
                    potential_password = next((g for g in match if g), match[0])
                else:
                    potential_password = match

                if len(potential_password) >= 6 and not self._is_blacklisted(potential_password):
                    found_passwords.append(potential_password)

        return list(set(found_passwords))  # Tekrarları temizle
