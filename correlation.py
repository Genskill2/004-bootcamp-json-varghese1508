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
        state = data[i]['squirrel']
        events = data[i]['events']

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

def compute_correlations():
    pass

def diagnose():
    pass