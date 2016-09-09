from datetime import datetime, date, time
from datetime import timedelta


class SleepTimeCalculator:
    
    def calculateWakeupTime(self, gotobedtime):
        # If I go to bed at particular time, when should I wake up?
        try:
            time = datetime.strptime(gotobedtime, '%H:%M')
        except:
            print("Unexpected error.")
            exit()
        wakeup = time + timedelta(hours=7, minutes=30) + timedelta(minutes=15) # 15 minutes in order to fall asleep
        wakeup = datetime.time(wakeup)
        return wakeup
    
    def calculateWakeupTimes(self, gotobedtime):
    # If I go to bed at particular time, when should I wake up?
        try:
            time = datetime.strptime(gotobedtime, '%H:%M')
        except:
            print("Unexpected error.")
            exit()
    
        wakeup = time + timedelta(minutes=15) # 15 minutes in order to fall asleep
        wakeupTimes = []
        for counter in range(0, 6, 1):
            wakeup = wakeup + timedelta(hours=1, minutes=30) #+ timedelta(minutes=15) # 15 minutes in order to fall asleep
            wakeupTimes.append(datetime.time(wakeup))
    
        return wakeupTimes
    
    def calculateGotobedTime(self, wakeuptime):
    # If I must wake up at particular time tomorrow, when should I go to bed?
        try:
            time = datetime.strptime(wakeuptime, '%H:%M')
        except:
            print("Unexpected error.")
            exit()
        wakeup = time - timedelta(hours=7, minutes=30) - timedelta(minutes=15) # 15 minutes in order to fall asleep
        wakeup = datetime.time(wakeup)
        return wakeup
    
    def calculateGotobedTimes(self, wakeuptime):
    # If I must wake up at particular time tomorrow, when should I go to bed?
        try:
            time = datetime.strptime(wakeuptime, '%H:%M')
        except:
            print("Unexpected error.")
            exit()
    
        wakeup = time - timedelta(minutes=15) # 15 minutes in order to fall asleep
        wakeupTimes = []
        wakeMeUpTimes = []
        for counter in range(0, 6, 1):
            wakeup = wakeup - timedelta(hours=1, minutes=30)
            wakeupTimes.append(datetime.time(wakeup))
        
        for counter in range(0, len(wakeupTimes), 1):
            wakeMeUpTimes.append(wakeupTimes[len(wakeupTimes) - counter - 1]) # Invert time list: from evening to morning
        
        return wakeMeUpTimes
    
    def getCurrentTime(self):
        today = datetime.today()
        currentTime = datetime.time(today)
        cTimeStr = str(currentTime.hour) + ":" + str(currentTime.minute)
        return cTimeStr

