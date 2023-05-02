# Install Python
Write-Host "Installing Python..."
$python_url = "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe"
$python_file = "$PWD\python-3.10.0-amd64.exe"
Invoke-WebRequest -Uri $python_url -OutFile $python_file
Start-Process -FilePath $python_file -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

# Add Python Scripts folder to system Path
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\Python310\Scripts", [EnvironmentVariableTarget]::Machine)

# Install Chrome
Write-Host "Installing Chrome..."
$chrome_url = "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B594AAB98-8D2C-6B66-6B58-678AEB12B1CA%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe"
$chrome_file = "$PWD\ChromeSetup.exe"
Invoke-WebRequest -Uri $chrome_url -OutFile $chrome_file
Start-Process -FilePath $chrome_file -ArgumentList "/silent /install" -Wait

[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\Windscribe", [EnvironmentVariableTarget]::Machine)