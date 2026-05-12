@echo off
echo Kutuphaneler yukleniyor...
py -m pip install -r requirements.txt
echo.
echo Program baslatiliyor...
py src/main.py
pause
