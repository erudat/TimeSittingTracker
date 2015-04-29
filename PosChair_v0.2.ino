int fsrPin_0 = 0;
int fsrPin_1 = 1;
int fsrPin_2 = 2;
int fsrPin_3 = 3;

int fsrRead_0;
int fsrRead_1;
int fsrRead_2;
int fsrRead_3;

int average01;
int average23;

void setup(void) {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop(void) {
  fsrRead_0 = analogRead(fsrPin_0);
  fsrRead_1 = analogRead(fsrPin_1);
  fsrRead_2 = analogRead(fsrPin_2);
  fsrRead_3 = analogRead(fsrPin_3);
  
  //  Serial.print("AnalogRead_ZERO = ");
  //  Serial.println(fsrRead_0);
  
  //  Serial.print("AnalogRead_ONE = ");
  //  Serial.println(fsrRead_1);
  
  //  Serial.print("AnalogRead_TWO = ");
  //  Serial.println(fsrRead_2);
  
  //  Serial.print("AnalogRead_THREE = ");
  //  Serial.println(fsrRead_3);
  
  average01 = (fsrRead_0 + fsrRead_1) / 2;
  average23 = (fsrRead_2 + fsrRead_3) / 2;
  
  // Conditional Handles Sending Data over Serial Port
  if (average01 >= average23) {
    Serial.println(average01);
  }
  else {
    Serial.println(average23);
  }
  
  // Conditional Handles Turning LED On/Off
  if (fsrRead_0 > 0 && fsrRead_1 > 0) {
    digitalWrite(13, HIGH);
  } else {
    digitalWrite(13, LOW);
  }
   
  if (fsrRead_2 > 0) {
    digitalWrite(12, HIGH);
  } else {
    digitalWrite(12, LOW);
  }
  
  delay(1000);
}
