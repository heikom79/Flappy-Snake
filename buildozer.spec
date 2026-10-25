[app]

# (str) Titel deiner App
title = Flappy Snake

# (str) Paketname (nur Kleinbuchstaben, keine Leerzeichen)
package.name = flappysnake

# (str) Paket-Domain
package.domain = org.arcade

# (str) Quellcode-Verzeichnis (wichtig zur Behebung des Fehlers)
source.dir = .

# (str) Versionsnummer der App (wichtig zur Behebung des Fehlers)
version = 0.1

# (str) Quellcode-Dateien
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = src/*, main.py

# (list) Anwendungsvoraussetzungen
requirements = python3,pygame

# (str) Einstiegspunkt der Anwendung
entrypoint = main.py

# (str) Ausrichtung
orientation = landscape

# (str) Unterstützte Android-Architekturen
android.archs = arm64-v8a, armeabi-v7a

# (int) Ziel-API-Level
android.api = 33

# (bool) Vollbildmodus
android.fullscreen = 1
