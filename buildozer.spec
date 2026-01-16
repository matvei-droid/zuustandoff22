[app]
title = zuulauncherso2
package.name = zuulauncherso2
package.domain = org.zuu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,hostpython3
orientation = portrait

# --- Android settings ---
android.api = 33
android.minapi = 21
# Убираем жесткую привязку к версиям NDK/SDK здесь, 
# так как мы пропишем пути в Workflow
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
