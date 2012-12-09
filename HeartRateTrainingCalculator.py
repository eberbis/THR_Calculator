#Based on the Karvonen Method of calculating THR.

print "\n\n############################################################################"
print "#                CALCULATOR OF YOUR TARGET HEART RATE (THR)                #"
print "#            (Based on the Karvonen Method of calculating THR.)            #"
print "#          http://www.wikihow.com/Calculate-Your-Target-Heart-Rate         #"
print "############################################################################"

age = int(raw_input('\nQ: What is your age?\nA: '))
rhr = int(raw_input('''\nQ: What is your Resting Heart Rate?
    (Remember that your RHR should be taken as the average of at least 3
    readings. These readings should be taken the morning after a day where
    you are rested, since trying to do it after a day of a hard workout can
    affect your results)\nA: '''))
HRmax = 220 - age
HRmaxReserve = HRmax - rhr
lowerTHR = (HRmaxReserve * 0.6) + rhr
upperTHR = (HRmaxReserve * 0.8) + rhr
THR = (lowerTHR + upperTHR) / 2
print "\n**************************"
print "*       RESULTS          *"
print "**************************"
print '''\n-> Your Maximum Heart Rate (HRmax) is: %s.
-> Your Heart Rate Reserve (HRmaxReserve) is: %s.
-> The lower limit of your THR is: %s.
-> The upper limit of your THR is: %s.
-> Your THR is: %s.''' % (HRmax, HRmaxReserve,
                       lowerTHR, upperTHR, THR)
