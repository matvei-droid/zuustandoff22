[app]
# Основная информация
title = zuulauncherso2
package.name = zuulauncherso2
package.domain = org.zuu

# Исходники
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Зависимости (hostpython3 критически важен для компиляции)
requirements = python3,kivy==2.3.0,hostpython3

orientation = portrait

# Настройки Android
android.api = 33
android.sdk = 33
android.minapi = 21
android.ndk = 25b
# Фиксируем версию инструментов, чтобы избежать ошибки с Aidl
android.build_tools_version = 33.0.0

# Разрешения
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Архитектура (для теста оставляем одну, так быстрее и надежнее)
android.archs = arm64-v8a

# Экран
android.fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
