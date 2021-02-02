import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


class Watererer:
    def __init__(self, measure_pin=14, water_pin=7):
        self.file = "sensordata"
        self.time = time.time()
        self.measure_pin = measure_pin
        self.water_pin = water_pin
        self.mode = "seconds"

    def start(self):
        self.main_loop()

    def main_loop(self):
        while True:
            time.sleep(1)
            ts = time.time()
            reading = self.measure()
            counter = 0
            time_start = 0
            time_end = 0

            print(ts, reading)

    def measure(self):
        counter = 0
        start_time = time.time()
        #Discharge
        GPIO.setup(self.measure_pin, GPIO.OUT)
        GPIO.setup(self.measure_pin, GPIO.LOw)
        time.sleep(0.1)
        GPIO.setup(self.measure_pin, GPIO.IN)
        while GPIO.input(self.measure_pin) == GPIO.LOW:
            counter += 1
        end_time = time.time()
        return start_time - end_time

    def water(self, seconds):
        if self.mode == "seconds":
            GPIO.output(self.water_pin, True)
            time.sleep(seconds)
            GPIO.output(self.water_pin, False)

