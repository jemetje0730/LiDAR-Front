@echo off
cd /d %~dp0
echo 🔄 프론트엔드 서버 실행 중...
start cmd /k "python frontend.py"
