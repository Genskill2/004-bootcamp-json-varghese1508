# Add the functions in this file
import json

def load_journal(fname: str) -> dict:
    f = open(fname,'r')     # opens file in write mode
    data = json.load(f)     # loads json file and returns dict of values
    return data

def compute_phi():
    pass

def compute_correlations():
    pass

def diagnose():
    pass