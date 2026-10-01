import numpy as np
from .validation import finite
def incidence_rate(cases,population,scale=100000):
    cases=finite(cases,"cases"); population=finite(population,"population")
    if cases.shape!=population.shape or (population<=0).any() or (cases<0).any(): raise ValueError("invalid counts")
    return cases/population*scale
def standardize(values):
    values=finite(values,"values"); sd=values.std(); return np.zeros_like(values) if sd==0 else (values-values.mean())/sd
def gravity_flow(pop_i,pop_j,distance,beta=2):
    if pop_i<0 or pop_j<0 or distance<=0 or beta<=0: raise ValueError("invalid gravity parameters")
    return float(pop_i*pop_j/(distance**beta))
def moran_input(cases,population): return standardize(incidence_rate(cases,population))
