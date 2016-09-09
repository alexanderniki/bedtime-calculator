
import sys
from waketime_calc import SleepTimeCalculator

'''
Usage:
$ wakeMeUp -wake 07:45
You need to go to bed at: 

$ wakeMeUp -sleep 01:30
It is better for you to wake up at:

$ wakeMeUp -sleep now
It is better for you to wake up at:
'''

def main():
    
    timeCalc = SleepTimeCalculator()

    if (len(sys.argv) == 3):
        mode = sys.argv[1]
        time = sys.argv[2]
        
        if (mode == "sleep"):
            if (time):
                if (str(time) == "now"):
                    print("If I go to bed right now, I should wake up at one of these times: ")
                    wakeupTimeList = timeCalc.calculateWakeupTimes(timeCalc.getCurrentTime())
                    for counter in range(0, len(wakeupTimeList), 1):
                        print(wakeupTimeList[counter])
                else:
                    print("If I go to bed at " + str(time) + ", I should wake up at one of these times: ")
                    for counter in range(0, len(timeCalc.calculateWakeupTimes(time)), 1):
                        print(timeCalc.calculateWakeupTimes(time)[counter])

        if (mode == "wake"):
            if (time):
                print("If I must wake up at " + str(time) + " tomorrow, I should go to bed at one of these times: ")
                for counter in range(0, len(timeCalc.calculateGotobedTimes(time)), 1):
                    print(timeCalc.calculateGotobedTimes(time)[counter])

    else:
        print("USAGE: wakeMeUp <mode> <HH:MM>")
    
if __name__ == '__main__':
    main()