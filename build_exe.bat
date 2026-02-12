@echo off
setlocal

REM Build a single-file Windows executable for the Deep Thought app.
REM Run this from Command Prompt in the project directory.

where py >nul 2>nul
if errorlevel 1 (
  echo [ERROR] Python launcher ^(py^) not found. Install Python 3 first.
  exit /b 1
)

py -m pip show pyinstaller >nul 2>nul
if errorlevel 1 (
  echo Installing PyInstaller...
  py -m pip install pyinstaller
  if errorlevel 1 (
    echo [ERROR] Failed to install PyInstaller.
    exit /b 1
  )
)

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist app.spec del /f /q app.spec

py -m PyInstaller --onefile --name DeepThoughtDispenser app.py
if errorlevel 1 (
  echo [ERROR] Build failed.
  exit /b 1
)

echo.
echo Build complete: dist\DeepThoughtDispenser.exe
echo Double-click that EXE, then open http://localhost:8000 in your browser.
