import datetime

def roundedTime(denominator: int = 5, roundUp: bool = True) -> str:
    time = datetime.datetime.now()
    timeString = time.strftime("%H:%M")
    if roundUp:
        roundedMinute = str(time.minute + (denominator - time.minute % denominator))
    else:
        roundedMinute = str(time.minute - (time.minute % denominator))
    return timeString[0:3] + roundedMinute
