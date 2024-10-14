import RPi.GPIO as GPIO
import time

# Định nghĩa các chân GPIO cho ba đèn giao thông
RED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22

# Cấu hình chế độ GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

def traffic_light():
    while True:
        # Bật đèn đỏ trong 5 giây
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(YELLOW_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        time.sleep(5)
        
        # Bật đèn vàng trong 2 giây
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        time.sleep(2)
        
        # Bật đèn xanh trong 5 giây
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        time.sleep(5)

try:
    traffic_light()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()