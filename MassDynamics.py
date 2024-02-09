"""Implemented by Federico Zocco
    Last update: 9 February 2024
    
Script to generate the results of Section 3.2 in [1].

References:
[1] Zocco, F., Sleath, D., and Rahimifard, S., 2024.
Towards a thermodynamical deep-learning-vision-based flexible 
robotic cell for circular healthcare. arXiv preprint arXiv:2402.05551.
[2] Zocco, F., Smyth, B. and Sopasakis, P., 2022. Circularity of 
thermodynamical material networks: Indicators, examples and algorithms. 
arXiv preprint arXiv:2209.15051.
[3] Cullen, J.M. and Cooper, D.R., 2022. Material flows and efficiency. 
Annual Review of Materials Research, 52, pp.525-559.
"""


import numpy as np
import matplotlib.pyplot as plt

### Parameters:
# (1) number of simulation steps 
n_final = 400   

# (2) parts of considered product 
frontCase = 14.4 # grams
backCase = 17.2
PCB = 17.8
screw = 0.2
numScrews = 5
spring = 0.1
buttonAndClip = 1.6
testStripPort = 1.0
screen = 8.4
USBportCap = 0.3 
GluMetMass = frontCase + backCase + PCB + screw*numScrews + spring + buttonAndClip + testStripPort + screen + USBportCap    

# (3) initial conditions
m1_ini = 2*GluMetMass
m2_ini = 0
m3_ini = 0 
m4_ini = 0 
m5_ini = 0 
m6_ini = 0
m12_ini = 0
m23_ini = 0
m24_ini = 0
m25_ini = 0
m26_ini = 0 

# (4) flows
m12_bar = GluMetMass
m23_bar = frontCase + backCase
m24_bar = PCB
m25_bar = screw*numScrews
m26_bar = spring + buttonAndClip + testStripPort + screen + USBportCap          
  
# (5) times
n1 = 5 
n2_in = 30 
n2_out_3 = 240
n2_out_4 = 300
n2_out_5 = 320
n2_out_6 = 360
flowTime = 5 # time it takes to move a material batch from vertex 2 to the designated bin 
n3_in = n2_out_3 + flowTime
n4_in = n2_out_4 + flowTime
n5_in = n2_out_5 + flowTime
n6_in = n2_out_6 + flowTime

   
 
### Discrete-time dynamics:
# vertex 1
m1_current = m1_ini
m1_new = [None]*n_final

for n in range(n_final):
    if n == n1:
        m1_new[n] = m1_current - m12_bar
    else:
        m1_new[n] = m1_current 
    m1_current = m1_new[n]

# vertex 2
m2_current = m2_ini
m2_new = [None]*n_final

for n in range(n_final):
    if n == n2_in:
        m2_new[n] = m2_current + m12_bar
    elif n == n2_out_3:
        m2_new[n] = m2_current - m23_bar
    elif n == n2_out_4:
        m2_new[n] = m2_current - m24_bar
    elif n == n2_out_5:
        m2_new[n] = m2_current - m25_bar
    elif n == n2_out_6:
        m2_new[n] = m2_current - m26_bar
    else:
        m2_new[n] = m2_current 
    m2_current = m2_new[n]

# vertex 3
m3_current = m3_ini
m3_new = [None]*n_final

for n in range(n_final):
    if n == n3_in:
        m3_new[n] = m3_current + m23_bar
    else:
        m3_new[n] = m3_current 
    m3_current = m3_new[n]

# vertex 4
m4_current = m4_ini
m4_new = [None]*n_final

for n in range(n_final):
    if n == n4_in:
        m4_new[n] = m4_current + m24_bar
    else:
        m4_new[n] = m4_current 
    m4_current = m4_new[n]

# vertex 5
m5_current = m5_ini
m5_new = [None]*n_final

for n in range(n_final):
    if n == n5_in:
        m5_new[n] = m5_current + m25_bar
    else:
        m5_new[n] = m5_current 
    m5_current = m5_new[n]

# vertex 6
m6_current = m6_ini
m6_new = [None]*n_final

for n in range(n_final):
    if n == n6_in:
        m6_new[n] = m6_current + m26_bar
    else:
        m6_new[n] = m6_current 
    m6_current = m6_new[n]
    
# arc 1,2
m12_current = m12_ini
m12_new = [None]*n_final

for n in range(n_final):
    if n == n1:
        m12_new[n] = m12_current + m12_bar
    elif n == n2_in:
        m12_new[n] = m12_current - m12_bar
    else:
        m12_new[n] = m12_current 
    m12_current = m12_new[n]

# arc 2,3
m23_current = m23_ini
m23_new = [None]*n_final

for n in range(n_final):
    if n == n2_out_3:
        m23_new[n] = m23_current + m23_bar
    elif n == n3_in:
        m23_new[n] = m23_current - m23_bar
    else:
        m23_new[n] = m23_current 
    m23_current = m23_new[n]
    
# arc 2,4
m24_current = m24_ini
m24_new = [None]*n_final

for n in range(n_final):
    if n == n2_out_4:
        m24_new[n] = m24_current + m24_bar
    elif n == n4_in:
        m24_new[n] = m24_current - m24_bar
    else:
        m24_new[n] = m24_current 
    m24_current = m24_new[n]
    
# arc 2,5
m25_current = m25_ini
m25_new = [None]*n_final

for n in range(n_final):
    if n == n2_out_5:
        m25_new[n] = m25_current + m25_bar
    elif n == n5_in:
        m25_new[n] = m25_current - m25_bar
    else:
        m25_new[n] = m25_current 
    m25_current = m25_new[n]
    
# arc 2,6
m26_current = m26_ini
m26_new = [None]*n_final

for n in range(n_final):
    if n == n2_out_6:
        m26_new[n] = m26_current + m26_bar
    elif n == n6_in:
        m26_new[n] = m26_current - m26_bar
    else:
        m26_new[n] = m26_current 
    m26_current = m26_new[n]
    


### Plots (NOTE: x axis in seconds since sample time T = 1 s):
# stocks
fig = plt.figure(figsize=(10, 10))
plt.plot(range(n_final), m1_new, 'r-', label = '$m_1$', linewidth=6)
plt.plot(range(n_final), m2_new, 'b-', label = '$m_2$', linewidth=6)
plt.plot(range(n_final), m3_new, 'g-', label = '$m_3$', linewidth=6)
plt.plot(range(n_final), m4_new, 'k-', label = '$m_4$', linewidth=6)
plt.plot(range(n_final), m5_new, 'm-', label = '$m_5$', linewidth=6)
plt.plot(range(n_final), m6_new, 'y-', label = '$m_6$', linewidth=6)
plt.plot(range(n_final), np.array(m1_new)+np.array(m2_new)+np.array(m3_new)+np.array(m4_new)+np.array(m5_new)+np.array(m6_new)+np.array(m12_new)+np.array(m23_new)+np.array(m24_new)+np.array(m25_new)+np.array(m26_new), 'r:', label = 'total', linewidth=6)
plt.grid() # if code is correct, mass within system is constant
plt.legend(loc='best', ncol= 2, prop={'size': 27}, bbox_to_anchor=(0.2,0.54))
plt.xlabel(r"Time, $t$ (s)", fontsize=35)
plt.ylabel(r"Stocks, (g)", fontsize=35)
plt.xticks(np.arange(min(range(n_final)), max(range(n_final+1))+1, 100), fontsize=35)
plt.yticks(fontsize=35)

# flows
fig = plt.figure(figsize=(10, 10))
plt.plot(range(n_final), m12_new, 'r-', label = '$m_{1,2}$', linewidth=6)
plt.plot(range(n_final), m23_new, 'b-', label = '$m_{2,3}$', linewidth=6)
plt.plot(range(n_final), m24_new, 'g-', label = '$m_{2,4}$', linewidth=6)
plt.plot(range(n_final), m25_new, 'k-', label = '$m_{2,5}$', linewidth=6)
plt.plot(range(n_final), m26_new, 'y-', label = '$m_{2,6}$', linewidth=6)
plt.grid()
plt.legend(loc='best', prop={'size': 27})
plt.xlabel(r"Time, $t$ (s)", fontsize=35)
plt.ylabel("Flows, (g)", fontsize=35)
plt.xticks(np.arange(min(range(n_final)), max(range(n_final+1))+1, 100), fontsize=35)
plt.yticks(fontsize=35)