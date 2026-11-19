[app]

title = Jogo 30 Seconds
package.name = jogo30seconds
package.domain = org.cinestro

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,wav,mp3,ogg

version = 1.0

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 1

android.api = 35
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

android.permissions = INTERNET

p4a.fork = kivy
p4a.branch = master


[buildozer]

log_level = 2
warn_on_root = 1
