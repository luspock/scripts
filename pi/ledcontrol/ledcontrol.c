#include <stdio.h>
#include <wiringPi.h>
#include <string.h>

int main(int argc, char *argv[]){
	char *parameter;
	if(argc!=2){
		printf("Usage: ledcontrol [on/off]\n");
		return -1;
	}
	wiringPiSetup();
	pinMode(7, OUTPUT);
	parameter = argv[1];
	if(strcmp(parameter,"on")==0)
		digitalWrite(7,HIGH);
	else digitalWrite(7,LOW);
	return 0;
}
