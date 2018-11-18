
#include <Wire.h>
#include "rgb_lcd.h"
//#include &lt;math.h&gt;
int a;
int maxaud=0;
float temperature;
int B=3975;                  //B value of the thermistor
float resistance;
String IncomingData = "";
String Temp = "";
char var;
int state=0;
int newstate=state;
int counter=0;

const int soundPin = A1; // sound input
const int lightPin1=A2; // light input
const int lightPin2=A3; // light input

const int ledPin=13;


rgb_lcd lcd;
int colorR = 0;
int colorG = 255;
int colorB = 0;

void setup() 
{
    Serial.begin(9600);
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    lcd.setRGB(colorR, colorG, colorB);
    

 //pinMode(humidPin, INPUT);
// pinMode(6, OUTPUT);
 // pinMode(ledPin,OUTPUT);

      delay(1000);
        //Serial.begin(115200);
    //Serial.println("Grove - Sound Sensor Test...");
}

void loop() 
{
    while(Serial.available())
  {
    var = Serial.read();
    Temp = String(var);
    IncomingData+= Temp;
  }
/*
  // LCD TEMP*************************************************************************
    // set the cursor to column 0, line 1
    lcd.setCursor(0, 0);
    // print the number of seconds since reset:
    //lcd.print(millis()/1000);

        a=analogRead(0);
    resistance=(float)(1023-a)*10000/a; //get the resistance of the sensor;
    temperature=1/(log(resistance/10000)/B+1/298.15)-273.15;//convert to temperature via datasheet&nbsp;;
     delay(5);
     lcd.print("Temp:      ");
     lcd.println((temperature* 9/5 + 32));

    delay(5);  
*/
   //Sound level***********************************
    long sum = 0;
    for(int i=0; i<32; i++)
    {
        sum += analogRead(soundPin);
    }

    sum >>= 5;
    

   Serial.println(sum);
   //         lcd.setCursor(0, 0);
   //        lcd.print("Audio Level: ");
   //  lcd.println(sum);
      
    lcd.setCursor(0,0);
    lcd.print("Noise: ");
  if(IncomingData!=""){
    lcd.println(IncomingData);
    lcd.setCursor(0,1);
    int ma = IncomingData.toInt();
    if(ma>=300){
      newstate=1;      
    }
    else{
      newstate=0;
    }
    if(newstate!=state){
      if(newstate>state){
        colorR = 255;
        colorG = 0;
        counter = 0;
        lcd.print("Noise!");
      }
    else if(state>newstate){
        colorR = 0;
        colorG = 255;
        lcd.print("      ");
      }
      lcd.setRGB(colorR, colorG, colorB);
    }
    if(newstate==1){
      counter = counter+1;
      lcd.print("Keep going! ");
      lcd.println(counter);
    }
    state = newstate;
    IncomingData="";
  }
 
   // delay(5);
   delay(100);
//Lights*******************************************



   int lightLevel1= analogRead(lightPin1);
   

   int lightLevel2= analogRead(lightPin2);

      
   
 
 
   // delay(5);
   delay(100);
//*******************************************



/*
const int ledPin=13;
void setup() {
    Serial.begin(9600);
    pinMode(ledPin,OUTPUT);
}

void loop() {
    int sensorState = digitalRead(2);
    Serial.println(sensorState);
    delay(100);
    if(sensorState == HIGH)
    {
        digitalWrite(ledPin,HIGH);
    }
    else
    {
        digitalWrite(ledPin,LOW);
    }
}
*/


}
