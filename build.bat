@echo off
rd /s /q build
rd /s /q dist
del randomvideo.spec
pyinstaller --windowed --name=randomvideo --icon=icon.ico --add-data="icon.png;." main.py