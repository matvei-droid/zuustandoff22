[app]

# (section) Title of your application
title = Zuu Optimizer

# (section) Package name
package.name = zuuoptimizer

# (section) Package domain (needed for android packaging)
package.domain = org.zuu

# (section) Source code where the main.py live
source.dir = .

# (section) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (section) Application version
version = 1.0

# (section) Application requirements
# Добавлен hostpython3 для стабильности сборки
requirements = python3,kivy,hostpython3

# (section) Supported orientations
orientation = portrait

# --- Android specific ---

# (section) Android API to use
# Используем API 33 (Android 13) как в твоем запросе
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# (section) Android permissions
# PACKAGE_USAGE_STATS часто ломает автоматическую сборку, 
# для начала соберем с базовыми правами.
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (section) Architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (section) Allow screen to be full screen
android.fullscreen = 0

# (section) Android logcat filters
android.logcat_filters = *:S python:D

# (section) Copy library instead of making a libpython.so
android.copy_libs = 1

# --- Buildozer settings ---
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
