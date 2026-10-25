[app]

# (str) Titel deiner App
title = Flappy Snake

# (str) Paketname (nur Kleinbuchstaben, keine Leerzeichen)
package.name = flappysnake

# (str) Paket-Domain (wichtig für Android-Eindeutigkeit)
package.domain = org.arcade

# (str) Quellcode-Dateien (inklusive des src-Ordners)
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = src/*, main.py

# (list) Anwendungsvoraussetzungen
# python3 und pygame sind hier das Wichtigste
requirements = python3,pygame

# (str) Einstiegspunkt der Anwendung
entrypoint = main.py

# (str) Ausrichtung (portrait oder landscape)
orientation = landscape

# (str) Unterstützte Android-Architekturen (armeabi-v7a und arm64-v8a decken fast alle modernen Handys ab)
android.archs = arm64-v8a, armeabi-v7a

# (int) Ziel-API-Level
android.api = 33

# (bool) Vollbildmodus
android.fullscreen = 1
