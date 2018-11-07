# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 19:36:35 2018

@author: K
"""
from ast import literal_eval

h=['phi','phi','phi','phi','phi','phi'] #most specific


#Training Data from a file
with open('C:/Users/K/data.txt') as f:  #path of file
    data = [list(literal_eval(line)) for line in f]

 
#l=['Rainy', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes']
    

def consistent(h,d):
    
    for i in range(len(h)):
            
            # Check if attribute in hypothesis and data instance are equal
            # Or it has '?' value.
            
            if ( not((h[i]==d[i]) or (h[i]=='?')) ):
                
                return False
                
    return True
    

#end of consistent()        

def makeConsistent(h,d):
    
    for i in range(len(h)):
        
        if((h[i] == 'phi')):
            
            #if hypothesis is phi, replace it with data
            h[i]=d[i]
            
            
            # if hypothesis ith value is not 'phi' and it is also not equal to ith value in data.
            
        elif(h[i]!=d[i]):
            
            # Replace ith value in hypothesis with '?'
            h[i]='?'
    
    # Return updated hypothesis
    return h
# end of makeConsistent(h,d)

#execution starts here
print('Start : Hypothesis :',h)
print('------------------------------------------')

for d in data:
    
    # Considering only 'Yes'
    
    if d[len(d)-1]=='Yes':
        
        # Checking consistency
        
        if (not(consistent(h,d))):
            
            # Previous hypothesis is compared with current data
            h=makeConsistent(h,d)
    
        #
        print ('Training Data         :',d)
        print ('New Hypothesis    :',h)
        print()
        print('********************************')
    
print('------------------------------------------')
print('Final Hypothesis :',h)