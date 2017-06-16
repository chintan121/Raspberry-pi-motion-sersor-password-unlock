import RPi.GPIO as GPIO
import time

PIR_OUT_PIN = 32  
BZRPin = 29

GPIO.setmode(GPIO.BOARD)       
GPIO.setup(PIR_OUT_PIN, GPIO.IN)  
GPIO.setmode(GPIO.BOARD)
if 1==1:
                        class keypad():
                                KEYPAD = [
                                [1,2,3,"A"],
                                [4,5,6,"B"],
                                [7,8,9,"C"],
                                ["*",0,"#","D"]
                                ]
                                                 
                                ROW         = [11,12,13,15]
                                COLUMN      = [16,18,22,7]
                              
                                 
                                def getKey(self):
                                         
                                        for j in range(len(self.COLUMN)):
                                                GPIO.setup(self.COLUMN[j], GPIO.OUT)
                                                GPIO.output(self.COLUMN[j], GPIO.LOW)
                                                         
                    
                                        for i in range(len(self.ROW)):
                                                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
                                                         
                                                      
                                        rowVal = -1
                                        for i in range(len(self.ROW)):
                                                tmpRead = GPIO.input(self.ROW[i])
                                                if tmpRead == 0:
                                                        rowVal = i
                                                                         
                                                    
                                        if rowVal < 0 or rowVal > 3:
                                                self.exit()
                                                return
                                                         
                                                        
                                        for j in range(len(self.COLUMN)):
                                                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                                                         
                                                
                                        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
                                        GPIO.output(self.ROW[rowVal], GPIO.HIGH)
                                         
                                        
                                        colVal = -1
                                        for j in range(len(self.COLUMN)):
                                                tmpRead = GPIO.input(self.COLUMN[j])
                                                if tmpRead == 1:
                                                        colVal=j
                                                                         
                                                       
                                        if colVal < 0 or colVal > 3:
                                                self.exit()
                                                return
                                         
                                                        
                                        self.exit()
                                        time.sleep(0.5)
                                        return self.KEYPAD[rowVal][colVal]
                                                         
                                def exit(self):
                                                       
                                        for i in range(len(self.ROW)):
                                                        GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
                                        for j in range(len(self.COLUMN)):
                                                        GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
                                               
                        kp = keypad()                                           
                        k=[7,7,7,7]
                        l=[4,3,2,1]


def loop():
        while True:
                
                if GPIO.input(PIR_OUT_PIN) == GPIO.LOW:
                        k=[7,7,7,7]
                        GPIO.cleanup(BZRPin)
                        print '...Movement not detected!'
                else:
                        while not (l[0]==k[-1]and l[1]==k[-2] and l[2]==k[-3] and l[3]==k[-4]):
                                print 'Movement detected!...'
        
                                digit = kp.getKey()
                                if not digit==None: 
                                        k.append (digit)
                                GPIO.setup(BZRPin, GPIO.OUT)
                                GPIO.output(BZRPin, GPIO.LOW)
                            
                                GPIO.output(BZRPin, GPIO.HIGH)
                                    

                                




                        

                                
                        

def destroy():
        GPIO.cleanup()                 

if __name__ == '__main__':     
        print'started'
        try:
                loop()
        except KeyboardInterrupt:  
                destroy()

