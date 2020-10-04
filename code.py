from scipy.stats import poisson
import random
TF=[]
TH=[]
TC=[]
WqF=[]
WqH=[]
WqC=[]
Fserver_busy = False
Hserver_busy = False
Cserver_busy = False
jh=0
jc=0
jf=0
qlc=[]
qlf=[]
qlh=[]
#random the type of coffee and number of customer each minutes
def rand(a,i):
    for k in range(0,a):
        rand=random.randint(0,10)
        if(rand>=7):
            TC.append(i)
        elif(rand>=4):
            TH.append(i)
        else:
            TF.append(i)
            
#simulation in i minutes
for i in range(0,780):
    qlf.append(len(TF))
    qlh.append(len(TH))
    qlc.append(len(TC))
    if i <=750:
        a=poisson.rvs(mu=1/3)
        rand(a,i)
    if not Fserver_busy and len(TF) > 0:
        Fserver_busy= True
        WqF.append(i-TF[0])
        del TF[0]
        jf=i+5
    if jf<=i:
        Fserver_busy = False 
        
    if not Cserver_busy and len(TC) > 0:
        Cserver_busy= True
        WqC.append(i-TC[0])
        del TC[0]
        jc=i+4
    if jc<=i:
        Cserver_busy = False
    
    if not Hserver_busy and len(TH) > 0:
        Hserver_busy= True
        WqH.append(i-TH[0])
        del TH[0]
        jh=i+3
    if jh<=i:
        Hserver_busy= False
print(sum(WqH)/len(WqH),'is expect waiting time of customer who order Hot coffee in queue')
print(sum(WqC)/len(WqC),'is expect waiting time of customer who order Cold coffee in queue')
print(sum(WqF)/len(WqF),'is expect waiting time of customer who order Frappe coffee in queue')     
print(max(qlf),',',max(qlh),',',max(qlc),'are maximum queue length of Frappe coffee, Hot coffee and Cold coffee respectivelly ')
