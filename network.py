import serial
from urllib.request import urlopen
arduino = serial.Serial('COM3', 9600)
data=''
while True:
        while (data!='\n'):
                data=arduino.readline()
                sent=data.decode('utf-8')
                val=sent.split(',')
                sen1=int(val[0])
                sen2=int(val[1])
                sen3=int(val[2])
                sen4=int(val[3])
                sen5=int(val[4])
                link='https://api.thingspeak.com/update?api_key=TRHCM5SL4FB9POU5&field1='+val[0]
                link2='https://api.thingspeak.com/update?api_key=TRHCM5SL4FB9POU5&field2='+val[1]
                link3='https://api.thingspeak.com/update?api_key=TRHCM5SL4FB9POU5&field3='+val[2]
                link4='https://api.thingspeak.com/update?api_key=TRHCM5SL4FB9POU5&field4='+val[3]
                link5='https://api.thingspeak.com/update?api_key=TRHCM5SL4FB9POU5&field5='+val[4]
                urlopen(link)
                urlopen(link2)
                urlopen(link3)
                urlopen(link4)
                urlopen(link5)
                print (sen1, sen2, sen3, sen4, sen5)
        print ("Hello")
