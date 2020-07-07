@echo off
setlocal enabledelayedexpansion

set folder_name=%1
set flag=%2
set status=%3
cd /d %~dp0

set cmd[0]=create folder_name          :    Use this format to create folder locally alongwith public repo on Github
set cmd[1]=create folder_name -l       :    Use this format to create folder only locally
set cmd[2]=create folder_name -g       :    Use this format to only create public repo on Github
set cmd[3]=create folder_name -pb      :    Use this format to create folder locally alongwith public repo on Github
set cmd[4]=create folder_name -lg      :    Use this format to create folder locally alongwith public repo on Github
set cmd[5]=create folder_name -gl      :    Use this format to create folder locally alongwith public repo on Github
set cmd[6]=create folder_name -pr      :    Use this format to create folder locally alongwith private repo on Github
set cmd[7]=create folder_name -g  -pb  :    Use this format to only create public repo on Github
set cmd[8]=create folder_name -g  -pr  :    Use this format to only create private repo on Github
set cmd[9]=create folder_name -lg -pb  :    Use this format to create folder locally alongwith public repo on Github
set cmd[10]=create folder_name -gl -pb  :    Use this format to create folder locally alongwith public repo on Github
set cmd[11]=create folder_name -lg -pr  :    Use this format to create folder locally alongwith private repo on Github
set cmd[12]=create folder_name -gl -pr  :    Use this format to create folder locally alongwith private repo on Github

if "%1"=="" (
    for /l %%n in (0,1,12) do ( 
        echo !cmd[%%n]! 
    )
) else ( 
    if "%1"=="--help" (
        for /l %%n in (0,1,12) do ( 
            echo !cmd[%%n]! 
        )
    ) else (
    python automate.py %folder_name% %flag% %status%
    ) 
)   