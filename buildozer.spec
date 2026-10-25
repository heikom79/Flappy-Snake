[app]

# (str) Titel deiner App
title = Flappy Snake

# (str) Paketname (nur Kleinbuchstaben, keine Leerzeichen)
package.name = flappysnake

# (str) Paket-Domain (wichtig für Android-Eindeutigkeit)
package.domain = org.arcade

# (str) Quellcode-Verzeichnis
source.dir = .

# (str) Versionsnummer der App
version = 0.1

# (str) Quellcode-Dateien
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = src/*, main.py

# (list) Anwendungsvoraussetzungen
requirements = python3,pygame

# (str) Einstiegspunkt der Anwendung
entrypoint = main.py

# (str) Ausrichtung (portrait oder landscape)
orientation = landscape

# (str) Unterstützte Android-Architekturen
android.archs = arm64-v8a, armeabi-v7a

# (int) Ziel-API-Level
android.api = 33

# (bool) Vollbildmodus
android.fullscreen = 1
