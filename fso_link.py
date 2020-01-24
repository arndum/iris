#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:25:29 2020

@author: arnauddumas
"""

import numpy as np
from scipy import special
import matplotlib.pyplot as plt

def bit_error_rate(snr_elec,threshold=0.5,plot_bool=0):
    '''
    computes bit error rate from SNR in gaussian noise assumption
    
    snr is expressed in electrical power
    
    amplitude is assumed unitary for bit = 1 and 0 for bit = 0
    
    recall that ber = proba(1|0) = proba(s>= threshold) = int_threshold^infty 1/sqrt(2 pi) * exp(-(s-s(0))^2/2 noise^2)
    
    @toffano, optoelectronique
    '''
    
    #amp = 1 
    #noise = 1./snr_elec
    
    # optical SNR  = 2xQ
    Q = 0.5*np.sqrt(snr_elec)
    ber = 0.5*special.erfc(Q/np.sqrt(2))
    
    if plot_bool:
        Q_vect = np.linspace(0,4,1000)
        ber_vect = 0.5*special.erfc(Q_vect/np.sqrt(2))
        fig,ax = plt.subplots(1)
        plt.plot(Q_vect,10*np.log(ber_vect)/np.log(10))
        plt.xlabel('0.5 x optical SNR')
        plt.ylabel('Bit error rate  [dB]')
        plt.title('BER vs SNR for gaussian noise')
        plt.grid(True)
    
    return ber 
    


if __name__ == "__main__":
    print('elementary test')
    bit_error_rate(10,plot_bool=1)
    







    