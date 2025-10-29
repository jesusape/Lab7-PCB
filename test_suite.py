import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_treshold=250# change this value
sound_treshold=750 # change this value


while True:
  print("Blinking 5 times")
  for _ in range(5):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.5)
  print("Detect Light")
  start= time.time()
  while time.time() - start < 5:  
      light_val=mcp.read_adc(0)   
      if light_val>lux_treshold:
          print("Light:", light_val, "bright")
      else:
          print("Light:", light_val, "dark")
      time.sleep(0.1)  
  print("Blink 4 times")
  for _ in range(4):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.2)
  print("Detecting Sound")
  print("Sound:", mcp.read_adc(1)) 
  time.sleep(0.5) 

  start=time.time()
  while time.time() - start < 5:
      sound_val = mcp.read_adc(1)
      print("Sound:", sound_val)
      if sound_val>sound_treshold:
          GPIO.output(11, GPIO.HIGH)
          time.sleep(0.1)
          GPIO.output(11, GPIO.LOW)
      time.sleep(0.1)


  #Following commands control the state of the output
  #GPIO.output(pin, GPIO.HIGH)
  #GPIO.output(pin, GPIO.LOW)

  # get reading from adc 
  # mcp.read_adc(adc_channel)
