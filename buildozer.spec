[app]
# Название приложения
title = Zuu Optimizer

# Имя пакета (маленькими буквами, без пробелов)
package.name = zuuoptimizer

# Домен организации
package.domain = org.zuu

# Исходный код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версия
version = 1.0

# Зависимости (Kivy обязателен для твоего кода)
requirements = python3,kivy

# Ориентация экрана
orientation = portrait

# --- Настройки Android ---

# Разрешения для работы с памятью и системой
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, PACKAGE_USAGE_STATS

# Соответствие версии твоего телефона (Android 13)
android.api = 35
android.minapi = 21
android.ndk = 25b
android.sdk = 33

# Архитектура процессора для Helio G88
android.archs = arm64-v8a, armeabi-v7a

# Полноэкранный режим (0 - выключен, 1 - включен)
android.fullscreen = 0

# --- Настройки сборки ---
[buildozer]
log_level = 2
warn_on_root = 1
