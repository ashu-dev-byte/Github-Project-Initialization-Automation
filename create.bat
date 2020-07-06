@echo off

set folder_name=%1
set flag=%2
cd /d %~dp0

set cmd01=create folder_name   :    Use this format to create folder locally only
set cmd02=create folder_name g :    Use this format to create repo on Github and locally

if "%1"=="" (
    echo %cmd01%
    echo %cmd02%
) else ( 
    if "%1"=="--help" (
        echo %cmd01%
        echo %cmd02%
    ) else (
    python automate.py %folder_name% %flag%
     ) 
  )   