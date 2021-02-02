import time
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import math

GPIO.setmode(GPIO.BCM)


class Watererer:
    def __init__(self, measure_pin=14, water_pin=7, sensor_gain=1):
        self.gain = sensor_gain
        self.adc = Adafruit_ADS1x15.ADS1x15()
        self.file = "sensordata"
        self.time = time.time()
        self.measure_pin = measure_pin
        self.water_pin = water_pin
        self.mode = "seconds"
        self.measure_values = 100

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
        values = []
        for i in range(self.measure_values):
            values[i] = self.adc.read_adc(0, self.gain)
        mean = sum(values) / self.measure_values
        return mean

    def water(self, seconds):
        if self.mode == "seconds":
            GPIO.output(self.water_pin, True)
            time.sleep(seconds)
            GPIO.output(self.water_pin, False)

