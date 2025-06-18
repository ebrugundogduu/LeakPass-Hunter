
const ANDROID_LOG_CLASSES = [
    'android.util.Log',
    'java.io.PrintStream',
];

const TARGET_METHODS = {
    'android.util.Log': ['d', 'i', 'w', 'e', 'v'],
    'java.io.PrintStream': ['println'],
};

// (İsteğe Bağlı) Uygulamaya özel metodlar için örnek yapı:
/*
const APP_SPECIFIC_CLASSES = {
    'com.example.vulnerableapp.AuthManager': ['loginUser', 'authenticate']
};
*/

function attachToLogMethods() {
    ANDROID_LOG_CLASSES.forEach(className => {
        try {
            const targetClass = Java.use(className);
            const methods = TARGET_METHODS[className];

            if (!targetClass || !methods) return;

            methods.forEach(methodName => {
                const overloads = targetClass[methodName].overloads;

                overloads.forEach(overload => {
                    overload.implementation = function (...args) {
                        let logMessage = '';

                        if (className === 'android.util.Log' && args.length >= 2) {
                            logMessage = args[1];
                        } else if (className === 'java.io.PrintStream' && args.length >= 1) {
                            logMessage = args[0];
                        } else if (args.length === 1) {
                            logMessage = args[0];
                        }

                        if (typeof logMessage === 'string' && logMessage.length > 0) {
                            send({
                                type: 'log_data',
                                timestamp: new Date().toISOString(),
                                source: `${className}.${methodName}`,
                                message: logMessage,
                            });
                        }

                        return overload.apply(this, args);
                    };
                });
            });
        } catch (e) {
            send({
                type: 'error',
                source: className,
                message: `Hooking error: ${e.message}`,
                time: new Date().toISOString()
            });
        }
    });

    /*
    // Uygulamaya özel metodlara hook atmak için (isteğe bağlı)
    for (const className in APP_SPECIFIC_CLASSES) {
        try {
            const targetClass = Java.use(className);
            const methods = APP_SPECIFIC_CLASSES[className];

            methods.forEach(methodName => {
                targetClass[methodName].overloads.forEach(overload => {
                    overload.implementation = function (...args) {
                        send({
                            type: 'method_call',
                            timestamp: new Date().toISOString(),
                            source: `${className}.${methodName}`,
                            args: args.map(arg => arg ? arg.toString() : '')
                        });
                        return overload.apply(this, args);
                    };
                });
            });
        } catch (e) {
            send({
                type: 'error',
                source: className,
                message: `App-specific hook error: ${e.message}`,
                time: new Date().toISOString()
            });
        }
    }
    */
}

Java.perform(function () {
    attachToLogMethods();
    send({
        type: 'status',
        message: 'LeakPass Hunter hooks initialized!',
        time: new Date().toISOString()
    });
});
