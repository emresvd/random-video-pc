@echo off
rd /s /q build
rd /s /q dist
pyinstaller --noconsole --name="randomvideo" --icon=icon.ico main.py