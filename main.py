import os
import subprocess
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

class ZuuOptimizer(App):
    def build(self):
        # Главный контейнер
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Заголовок и Инфо-панель
        self.info_label = Label(
            text="Загрузка данных...", 
            size_hint_y=None, 
            height=250, 
            halign="center", 
            markup=True,
            font_size='14sp'
        )
        self.main_layout.add_widget(self.info_label)
        
        # Обновление данных системы каждые 2 секунды
        Clock.schedule_interval(self.update_system_info, 2)

        # Сетка для 36 кнопок (2 колонки)
        scroll_view = ScrollView()
        self.grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        # Список функций (Название: Команда)
        # Примечание: Команды взяты из твоего исходного .sh скрипта
        self.commands = {
            "1. CPU Boost 🚀": "stop thermal-engine; stop vendor.thermal-engine; setprop thermal.control 0; for cpu in /sys/devices/system/cpu/cpu[0-9]*; do echo performance > $cpu/cpufreq/scaling_governor; done",
            "2. Unlock 120Hz 📱": "pm disable-user com.xiaomi.joyose; settings put global min_refresh_rate 120.0",
            "3. ULTRA SO2 🎮": "setprop persist.vendor.max.fps 120; am force-stop com.axlebolt.standoff2",
            "4. Reset All 🔄": "settings put global min_refresh_rate 60.0; pm enable com.xiaomi.joyose",
            "5. GPU Turbo ⚡": "setprop debug.egl.hw 1; setprop debug.cpurender.force_opengl 1",
            "6. Sens Fix 🎯": "setprop touch.pressure.scale 0.001; setprop view.scroll_friction 0.001",
            "7. Network Opt 🌐": "setprop net.tcp.buffersize.wifi 4096,87380,110208,4096,16384,110208",
            "8. Thermal Off ❄️": "stop thermal-engine; setprop thermal.control 0",
            "9. Unity Opt 🛠️": "setprop ro.unity.fps_max 120",
            "10. DNS Google 🔍": "setprop net.dns1 8.8.8.8; setprop net.dns2 8.8.4.4",
            "11. Clean Cache 🧹": "rm -rf /data/local/tmp/*",
            "12. Trim /Data 📉": "fstrim -v /data",
            "13. HZ Lock 120 🔓": "settings put system min_refresh_rate 120.0",
            "14. Task Killer 💀": "ps -ef | grep -v 'root|termux|sh' | awk '{print $2}' | xargs kill -9",
            "15. DEX Opt SO2 📦": "cmd package compile -m speed-profile com.axlebolt.standoff2",
            "16. Stop LOGD 🛑": "stop logd; stop logcatd",
            "17. ZRAM Reset 🔋": "swapoff /dev/block/zram0; echo 1 > /sys/block/zram0/reset; swapon /dev/block/zram0",
            "18. Ultra Cool 🧊": "for cpu in /sys/devices/system/cpu/cpu[0-9]*; do echo powersave > $cpu/cpufreq/scaling_governor; done",
            "19. Low Power 🔋": "setprop power.save.mode 1",
            "20. EXIT 🚪": "exit",
            "21. Ping Fix 📡": "setprop net.dns1 1.1.1.1; setprop net.dns2 1.0.0.1",
            "22. I/O Boost 🏎️": "for d in /sys/block/*/queue/read_ahead_kb; do echo 2048 > $d; done",
            "23. Deep Clean 🧽": "rm -rf /sdcard/Android/data/com.axlebolt.standoff2/cache/*",
            "24. Fix Props 🔧": "setprop ro.product.model 'SM-S908B'; setprop ro.product.brand 'Samsung'",
            "25. Lang Switch 🇷🇺": "echo 'Lang toggled'",
            "26. Zuu TG ✉️": "am start -a android.intent.action.VIEW -d 'https://t.me/zuu_tg'",
            "27. Net Pro 📶": "setprop net.tcp.nodelay 1; settings put global wifi_scan_always_enabled 0",
            "28. Hard Comp 💎": "cmd package compile -m speed -f com.axlebolt.standoff2",
            "29. No Doze 😴": "dumpsys deviceidle disable",
            "30. RAM Master 🧠": "echo 10 > /proc/sys/vm/dirty_ratio; echo 0 > /proc/sys/vm/swappiness",
            "31. Touch Pro 👆": "setprop windowsmgr.max_events_per_sec 240; settings put system pointer_speed 7",
            "32. Ghost Clean 👻": "rm -rf /data/tombstones/*; stop logd",
            "33. SO2 Priority 🔝": "renice -n -20 -p $(pidof com.axlebolt.standoff2)",
            "34. SQL Optimize 🗃️": "find /data/data/com.axlebolt.standoff2 -name '*.db' -exec sqlite3 {} 'VACUUM;' \;",
            "35. GFX Overlay 🖼️": "setprop debug.hwui.profile visualizer",
            "36. FS Speedup ⚡": "echo 0 > /proc/sys/vm/page-cluster; setprop persist.sys.scrolling_cache 3"
        }

        for name, cmd in self.commands.items():
            btn = Button(text=name, size_hint_y=None, height=120)
            btn.bind(on_release=lambda x, c=cmd: self.run_cmd(c))
            self.grid.add_widget(btn)

        scroll_view.add_widget(self.grid)
        self.main_layout.add_widget(scroll_view)
        return self.main_layout

    def run_cmd(self, command):
        if command == "exit":
            App.get_running_app().stop()
        else:
            # Выполнение через Root (su)
            subprocess.run(['su', '-c', command], shell=False)

    def update_system_info(self, dt):
        try:
            # Чтение температуры (упрощенно)
            temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").read().strip()
            temp = f"{int(temp)/1000:.1f}°C" if temp else "? °C"
            
            # Свободная RAM
            mem = os.popen("grep MemAvailable /proc/meminfo").read().split()
            mem = f"{int(mem[1])//1024} MB" if mem else "? MB"

            self.info_label.text = f"[b][color=00ff00]ZUU OPTIMIZER[/color][/b]\n[color=33ffff]Temp:[/color] {temp} | [color=33ffff]Free RAM:[/color] {mem}\n[color=ff3333]Root Status:[/color] Active"
        except:
            self.info_label.text = "Ошибка получения данных"

if __name__ == '__main__':
    ZuuOptimizer().run()

 
