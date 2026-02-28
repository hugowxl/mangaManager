@echo off
chcp 65001 >nul
set PORT=8000

echo 正在查找占用端口 %PORT% 的进程...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":%PORT%" ^| findstr "LISTENING"') do (
    echo 终止进程 PID: %%a
    taskkill /PID %%a /F
)

echo 完成.
pause
