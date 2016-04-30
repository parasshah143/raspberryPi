#include <wiringPi.h>
#include <stdio.h>
int main (void)
{
	wiringPiSetup ();
	pinMode (8, OUTPUT);
	pinMode (9, OUTPUT);
	pinMode (7, OUTPUT);
	pinMode (0, OUTPUT);
	for (;;)
	{
		
		digitalWrite (8, HIGH);
		delay (300);
		digitalWrite (8, LOW);
		delay (300);

		digitalWrite (9, HIGH);
		delay (300);
		digitalWrite (9, LOW);
		delay (300);

		digitalWrite (7, HIGH);
		delay (300);
		digitalWrite (7, LOW);
		delay (300);

		digitalWrite (0, HIGH);
		delay (300);
		digitalWrite (0, LOW);
		delay (300);
	}
	return 0 ;
}
