[app]
title = zuulauncherso2
package.name = zuulauncherso2
package.domain = org.zuu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,hostpython3
orientation = portrait
android.api = 33
android.minapi = 21
android.ndk = 25b
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
