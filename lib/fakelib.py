########################################################################
# Fake library used to develop RPi-Monitor-LCD in Ubuntu
########################################################################
def wiringPiSetup():
  print "wiringPiSetup()"
    
def mcp23017Setup(PIN_BASE,I2C_ADDR):
  print "mcp23017Setup"

def pinMode(PIN_BASE,INPUT):
  print "pinMode"
  
def pullUpDnControl(PIN_BASE,PUD_UP):
  print "pullUpDnControl"
  
def init():
  print "init"

def cls():
  print "cls"
  
def backlight(ON):
  print "backlight"

def digitalRead(button):
  pass
  
def delay(delay):
  pass
