import os
from pathlib import Path
import subprocess

def create_virtualenv():
    
    subprocess.run(['python', '-m', 'venv', 'venv'])
    if os.name == 'posix':
        subprocess.run(['source', str(Path('venv', 'bin', 'activate'))], shell = True)
        
    elif os.name == 'nt':
        subprocess.run([str(Path('venv', 'scripts', 'activate'))], shell = True)

def install_dependencies():
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

def deploy_application():
    subprocess.run(['python', 'main.py'])

def main():
    print("Starting deployment...")
    print("Creating virtual environment...")
    create_virtualenv()
    print("Installing dependencies...")
    install_dependencies()
    print("Deploying application...")
    deploy_application()
    print("Deployment complete.")

if __name__ == "__main__":
    main()