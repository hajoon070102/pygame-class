@echo off

 
:: 가상환경 디렉토리 설정
set VENV_DIR=.venv


:: 가상환경 생성 여부 확인
echo Checking for virtual environment...
echo ---------------------------------------------------
if not exist %VENV_DIR% (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
    echo Virtual environment created.
) else (
    echo Using existing virtual environment.
)
echo ---------------------------------------------------


:: 가상환경 활성화
echo Activating virtual environment...
echo ---------------------------------------------------
call %VENV_DIR%\Scripts\activate


:: 패키지 설치
echo Installing packages from requirements.txt...
:: Check if requirements.txt exists
if not exist requirements.txt (
    echo requirements.txt not found.
    echo Installing default packages: pygame, black, isort...
    pip install pygame black isort
    echo Saving installed packages to requirements.txt...
    pip freeze > requirements.txt
) else (
    :: Install packages from requirements.txt
    echo Installing packages from requirements.txt...
    pip install -r requirements.txt
)
echo ---------------------------------------------------


echo Virtual environment setup and package installation complete.
echo ---------------------------------------------------
pause
