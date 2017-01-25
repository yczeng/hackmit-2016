/*

  PrezGo

  sound from red then green is the directionality
  180 1.0
  90  0.71
  60  0.5


*/

#include <math.h>                              //Sets up needed libraries
#include <LiquidCrystal.h>
#include <Keyboard.h>
#include <Mouse.h>



int red = 2;              //Sets up IO pins for the microphone input
int green = 3;
int cswitch = 4;
int mswitch = 5;

unsigned long rtime;       //Point in time of each
unsigned long gtime;
unsigned long previousclaptime;

unsigned long neg = 1000000;

int redtag;      //Used in algorithm to account for microphones
int greentag;

int resetkey;



unsigned long maxdelay = 1600;

unsigned long limit = maxdelay * 2;           //in microseconds

int echotime = 100;     //A generic wait time, ie for echos in milliseconds
int betweentime = 200000;   //The time period between which there should be no noises
unsigned long endclaptime = 700000;

int clapcount;   //Counts the number of claps
int anglerange = 3;  //3  = 180, 2 = 90, 1 = 60

int serava;
int action;

byte uiBytes[] = {0, 1, 0, 2, 0, 3, 0, 4, 0, 1, 0, 3};

void setup()
{
  Serial.begin(9600);

  Keyboard.begin();

  pinMode(red, INPUT);
  pinMode(green, INPUT);
  pinMode(cswitch, INPUT);
  pinMode(mswitch, INPUT);

  digitalWrite(red, LOW);
  digitalWrite(green, LOW);
  digitalWrite(cswitch, LOW);
  digitalWrite(mswitch, LOW);

  delay(echotime);
}


void loop()  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
{
lstart:

  if (resetkey)
  {
    Serial.println("resetn ");

    rtime = 0;
    gtime = 0;
    redtag = 0;
    greentag = 0;

    resetkey = 0;
  }

  if (digitalRead(red) && digitalRead(cswitch) && !redtag)
  {
    rtime = micros();
    redtag = 1;
    Serial.println("red ");
  }

  else if (digitalRead(green) && digitalRead(cswitch) && !greentag)
  {
    gtime = micros();
    greentag = 1;
    Serial.println("green ");
  }

  else if (redtag && greentag)                       //If both claps register within the time
  {
    Serial.println("both ");
    delay(echotime);
    Serial.println(gtime - rtime);


    if (gtime - rtime > neg)   //> neg means it is negative
    {
      Serial.println("wdirection ");
      resetkey = 1;
      goto lstart;
    }

    if (gtime - rtime > maxdelay)
    {
      Serial.println("bfailed ");
      Serial.println(gtime - rtime);
      resetkey = 1;
      goto lstart;
    }


    if ((gtime - rtime) < (float(maxdelay) * 1) && (anglerange == 3))
    {
      if (micros() - gtime < betweentime)
      {
        resetkey = 1;
        goto lstart;
      }
      Serial.println("fullclap ");
      clapcount = clapcount + 1;
      previousclaptime = micros();
      resetkey = 1;
      goto lstart;
    }

    if ((gtime - rtime) > (float(maxdelay) * 0.71) && (anglerange == 2))
    {
      if (micros() - gtime < betweentime)
      {
        resetkey = 1;
        goto lstart;
      }
      Serial.println("fullclap ");
      clapcount = clapcount + 1;
      previousclaptime = micros();
      resetkey = 1;
      goto lstart;
    }

    if ((gtime - rtime) > (float(maxdelay) * 0.5) && (anglerange == 1))
    {
      if (micros() - gtime < betweentime)
      {
        resetkey = 1;
        goto lstart;
      }
      Serial.println("fullclap ");
      clapcount = clapcount + 1;
      previousclaptime = micros();
      resetkey = 1;
      goto lstart;
    }

    resetkey = 1;
    goto lstart;
  }

  else if ((((micros() - rtime) > limit) && redtag) || (((micros() - gtime) > limit) && greentag))  //Timed out after one microphone
  {
    Serial.println("onemictimeout ");
    delay(echotime);
    resetkey = 1;
    goto lstart;
  }

  else if ((micros() - previousclaptime > endclaptime) && (clapcount > 0))     //Timed out after final clap
  {
    Serial.println("finalclap ");
    delay(echotime);


    if (clapcount == 1)
    {
      action = uiBytes[1];
      if (digitalRead(mswitch) == LOW)
      {
        Serial.println("spaceprint ");
        Keyboard.print(" ");
      }
    }

    if (clapcount == 2)
    {
      action = uiBytes[3];
      if (digitalRead(mswitch) == LOW)
      {
        Serial.println("jprint ");
        Keyboard.print("j");
      }
    }

    if (clapcount == 3)
    {
      action = uiBytes[5];
      if (digitalRead(mswitch) == LOW)
      {
        Serial.println("lprint ");
        Keyboard.print("l");
      }
    }

    if (clapcount == 4)
    {
      action = uiBytes[7];
      if (digitalRead(mswitch) == LOW)
      {
        Serial.println("mprint ");
        Keyboard.print("m");
      }
    }

    if (digitalRead(mswitch) == HIGH)
    {
      if (action == 1)

      {
        Serial.println("nprint ");
        Keyboard.print("n");
      }
      if (action == 2)
      {
        Serial.println("pprint ");
        Keyboard.print("p");
      }
      if (action == 3)
      {
        Serial.println("pppprint ");
        Keyboard.print("p");
        delay(200);
        Keyboard.print("p");
        delay(200);
        Keyboard.print("p");
      }
      if (action == 4)
      {
        Serial.println("bprint ");
        Keyboard.print("b");
      }
    }



    Serial.println("resetall ");
    clapcount = 0;

    resetkey = 1;
    goto lstart;
  }

  delayMicroseconds(5);


  while (digitalRead(cswitch) == LOW)
  {


    serava = Serial.available();
    if (serava > 0)
    {
      for (int n = 0; n < serava; n++)
      {
        uiBytes[n] = Serial.read() - 48;
      }
      Serial.print("I received: ");
      for (int n = 0; n < 12; n++)
      {
        Serial.println(uiBytes[n]);
      }


    }


  }



}
