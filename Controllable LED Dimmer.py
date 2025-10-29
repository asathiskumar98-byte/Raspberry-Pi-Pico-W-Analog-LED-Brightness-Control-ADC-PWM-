import machine
from machine import ADC
from machine import Pin, PWM
import time

adc = ADC(0)

led = machine.Pin(17,machine.Pin.OUT)  #LED
pwm  = machine.PWM(led)
pwm.freq(5000)  # Freq PWM = 5000Hz

pwm  = machine.PWM(led)

while True:
    adc_value = adc.read_u16()  # 0 - 65535
    print('ADC_Value:',adc_value)
    pwm.duty_u16(adc_value)  # 0 = 0% 65535 = 100%
    time.sleep(0.2)
    
