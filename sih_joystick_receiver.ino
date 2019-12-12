#define enA 9
#define in1 4
#define in2 5
#define enB 10
#define in3 2
#define in4 3
int motorSpeedA = 0;
int motorSpeedB = 0;
#include "VirtualWire.h"
byte message[VW_MAX_MESSAGE_LEN]; // a buffer to store the incoming messages
byte messageLength = VW_MAX_MESSAGE_LEN; // the size of the message
int count;
int i;
void setup() {
  // put your setup code here, to run once:
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  Serial.begin(9600);
  vw_set_rx_pin(12);       //Sets pin D0 as the RX Pin
  vw_set_ptt_inverted(true); // Required for DR3100
  vw_setup(4000);      // Bits per sec
  vw_rx_start();       // Start the receiver PLL running
}

void loop() {
  // put your main code here, to run repeatedly:




}
