# Add the functions in this file
import json
import math

def load_journal(fname: str) -> dict:
    f = open(fname,'r')     # opens file in write mode
    data = json.load(f)     # loads json file and returns dict of values
    return data

def compute_phi(data: dict, event: str) -> float:
    corr = 0.0
    n00,n01,n10,n11 = 0,0,0,0
    np1,np0,n1p,n0p = 0,0,0,0

    for i in range(len(data)):
        state = dict(data[i])['squirrel']
        events = dict(data[i])['events']

        if state==True:
            np1+=1
        else:
            np0+=1

        if event in events:
            n1p+=1

            if(state):      # both are true
                n11+=1
            else:           # event happend, not transformation
                n10+=1

        else:
            n0p+=1

            if(state):  # event didn't happen, transformation happpend
                n01+=1
            else:       # both are false
                n00+=1

    corr = ((n11*n00)-(n01*n10))/ math.sqrt(np1*np0*n1p*n0p)

    return corr

def compute_correlations(fname: str) -> dict:
    data = load_journal(fname)
    eventPhi = {}

    for i in range(len(data)):
        events = data[i]['events']
        for event in events:
            if event not in eventPhi:
                eventPhi[event] = compute_phi(data,event)

    return eventPhi

def diagnose(fname: str) -> dict:
    eventPhi = compute_correlations(fname)
    result = []

    Max,Min = -2,2
    maxEvent,minEvent = "",""

    for event in eventPhi:
        if(eventPhi[event]<Min):
            Min = eventPhi[event]
            minEvent = event
        elif(eventPhi[event]>Max):
            Max = eventPhi[event]
            maxEvent = event

    result.append(maxEvent)
    result.append(minEvent)

    return result