@echo off
rd /s /q build
rd /s /q dist
del randomvideo.spec
pyinstaller --noconsole --name=randomvideo --icon=icon.ico --add-data="icon.png;." --add-data="icon.ico;." main.py
