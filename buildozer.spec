[app]
# Название приложения
title = zuulauncherso2
# Имя пакета
package.name = zuulauncherso2
# Домен организации
package.domain = org.zuu

# Исходный код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Зависимости
requirements = python3,kivy==2.3.0,hostpython3

orientation = portrait

# Настройки Android
android.api = 33
android.sdk = 33
android.minapi = 21
android.ndk = 25b
# Фиксируем версию build-tools, чтобы избежать ошибки с Aidl (36.1)
android.build_tools_version = 33.0.0

# Разрешения
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Архитектура (для стабильности оставляем одну)
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
