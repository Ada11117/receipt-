#importing necessary modules 

import subprocess, time, os
from simple_colors import *
ac=0
bc=0
cc=0
dc=0
ec=0
fc=0
gc=0
hc=0
ic=0
jc=0
chca=[]
tc=0
z7=[]
a7=[]
b7=[]
c7=[]
d7=[]
e7=[]
f7=[]
g7=[]
h7=[]
i7=[]
j7=[]
z8=[]
name=""

#choose to enter or exit
def name( ):
    global name
    name=input("Enter Your Name : ")
    choose()
    
def choose( ):
    subprocess.run('clear',shell=True)
    c1="1. Enter The Supermarket"
    c2="2. Exit"
    print(magenta(c1))
    print(magenta(c2))
    ch=int(input(cyan("Enter 1 or 2 : ")))
    if ch==1:
        grocery( )
    if ch==2:
        subprocess.run('clear',shell=True)
        print(magenta("Thanks for coming, Come again soon..."))
    if ch>2 or ch<1:
        print("Wrong Input")  
        
#All Items       
   
def grocery( ):
    don="done"
    don=don.upper()
    subprocess.run('clear',shell=True)
    print(cyan("            Welcome To Goatlion Industries\n\n",'bold'))
    global chca, z7, a7, b7, c7, d7, e7, f7, g7, h7, i7, j7, ac, bc, cc, dc, ec, fc, gc, hc, ic, jc,z8   
    z7="          Item                   Price (INR)\n"
    z8="          Item                   Price (INR)"
    a7="          A. Cricket Bat          499"
    b7="          B. Football             999"
    c7="          C. Perfume               49"
    d7="          D. Football Boots      2999"
    e7="          E. Blanket              399"
    f7="          F. Brown Bread          100"
    g7="          G. Keyboard            2999"
    h7="          H. Kissan Jam           100"
    i7="          I. School Bag           599"
    j7="          J. Peanut Butter        199"
    j8="          K. Other Item           ---  "
    print(z7)
    print(a7)
    print(b7)
    print(c7)
    print(d7)
    print(e7)
    print(f7)
    print(g7)
    print(h7)
    print(i7)
    print(j7)
    print(j8)
    print(yellow("- Quantity is limited to 5 only"))
    while True:
        print("\n")
        chca=input(red("Enter option to buy : "))
        chca=chca.upper()
        if chca=="A":
            chcq=int(input(yellow("Enter Quantity : ")))
            if chcq>0 or chcq<6:
                ac=499*chcq    
        if chca=="B":
            chcq=int(input(yellow("Enter Quantity : ")))
            if chcq>0 or chcq<6:
                bc=999*chcq
        if chca=="C":
            chcq=int(input(yellow("Enter Quantity : ")))
            if chcq>0 or chcq<6:
                cc=49*chcq
        if chca=="D":
            chcq=int(input(yellow("Enter Quantity : ")))
            if chcq>0 or chcq<6:
                dc=2999*chcq
        if chca=="E":
            chcq=int(input(yellow("Enter Quantity : ")))
            if chcq>0 or chcq<6:
                ec=399*chcq
        if chca=="F":
            chcq=int(input(yellow("Enter Quantity : ")))
            if chcq>0 or chcq<6:
                fc=100*chcq
        if chca=="G":
            chcq=int(input(yellow("Enter Quantity : ")))
            if chcq>0 or chcq<6:
                gc=2999*chcq
        if chca=="H":
            chcq=int(input(yellow("Enter Quantity : ")))
            if chcq>0 or chcq<6:
                hc=100*chcq
        if chca=="I":
            chcq=int(input(yellow("Enter Quantity : ")))
            if chcq>0 or chcq<6:
                ic=599*chcq     
        if chca=="J":
            chcq=int(input(yellow("Enter Quantity : ")))
            if chcq>0 or chcq<6:
                jc=199*chcq
        if chca=="K":
             xp=input(yellow("Enter Item : "))
             if xp=="abcde":
                      print(magenta("-  Out of Stock"))
                      print("Wait for 3 sec.....")
                      time.sleep(3)
             else:
                  print(magenta("-  Out of stock"))
                  print("-  Wait for 3 sec.....")
                  time.sleep(3)                             
        if chca==don:
            subprocess.run('clear',shell=True)
            inp=int(input(cyan("Enter 1 for printing reciept : ")))
            if inp==1:
                reciept()
            else:
                print("Wrong Input")
                choose()     
            break  

                                    
#reciept for purchased items 
    
def reciept( ):
    hour=time.strftime('%H')
    min=time.strftime('%M')
    date=time.strftime('%D')
    subprocess.run('clear',shell=True)
    global ac, bc, cc, dc, ec, fc, gc, hc, ic, jc, tc, z7, a7, b7, c7, d7, e7, f7, g7, h7, i7, j7, name, z8  
    dash="          ------------------------------------               "
    nl="\n"
    file=open("recordsmarket.txt","a+")
    itp="Items purchased by "+name+"-\n"
    file.write(dash) 
    file.write(itp)
    file.write(nl)
    print("                 GOATLION INDUSTRIES                     ")
    print("                                  ",date)
    print("                                   ",hour,":",min)
    print
    print("                    Near M.J Road                           ")
    print("          ------------------------------------               ")
    print(z8)
    print("          ------------------------------------               ")
    if ac==499:
        print(a7)
        file.write(a7)
        file.write(nl)
    if ac==998:
        print(a7,"  ×2")
        qq=a7+"  x2"
        file.write(qq)
        file.write(nl)
    if ac==1497:
        print(a7, "  ×3")
        qw=a7+"  ×3"
        file.write(qw)
        file.write(nl)
    if ac==1996:
        print(a7,"  ×4")
        qe=a7+"  ×4"
        file.write(qe)
        file.write(nl)
    if ac==2495:
        print(a7,"  ×5")
        qr=a7+"  ×5"
        file.write(qr)
        file.write(nl)
    if ac>2495:
        ac=2495
        print(a7,"  ×5")
        qt=a7+"  ×5"
        file.write(qt)
        file.write(nl)
        print("          :Stock is limited to 5 only")         
            
#Item B B B B B B B B B B B B                         
    if bc==999:
        print(b7)
        file.write(b7)
        file.write(nl)
    if bc==1998:
        print(b7,"  ×2")
        qy=b7+"  ×2"
        file.write(qy)
        file.write(nl)
    if bc==2997:
        print(b7, "  ×3")
        qu=b7+"  ×3"
        file.write(qu)
        file.write(nl)
    if bc==3996:
        print(b7,"  ×4")
        qi=b7+"  ×4"
        file.write(qi)
        file.write(nl)
    if bc==4995:
        print(b7,"  ×5")
        qo=b7+"  ×5"
        file.write(qo)
        file.write(nl)
    if bc>4995:
        bc=4995
        print(b7,"  ×5")
        qp=b7+"  ×5"
        file.write(qp)
        file.write(nl)
        print("          :Stock is limited to 5 only")            
    
# item C C C C C C C C C C C  C
    
    if cc==49:
        print(c7)
        file.write(c7)
        file.write(nl)
    if cc==98:
        print(c7,"  ×2")
        qa=c7+"  ×2"
        file.write(qa)
        file.write(nl)
    if cc==147:
        print(c7, "  ×3")
        qs=c7+"  ×3"
        file.write(qs)
        file.write(nl)
    if cc==196:
        print(c7,"  ×4")
        qd=c7+"  ×4"
        file.write(qd)
        file.write(nl)
    if cc==245:
        print(c7,"  ×5")
        qf=c7+"  ×5"
        file.write(qf)
        file.write(nl)
    if cc>245:
        cc=245
        print(c7,"  ×5")
        qg=c7+"  ×5"
        file.write(qg)
        file.write(nl)
        print("          :Stock is limited to 5 only")    
    
# item D D D D D  D D D D D  D D D D   D 

    if dc==2999:
        print(d7)
        file.write(d7)
        file.write(nl)
    if dc==5998:
        print(d7,"  ×2")
        qh=d7+"  ×2"
        file.write(qh)
        file.write(nl)
    if dc==8997:
        print(d7, "  ×3")
        qj=d7+"  ×3"
        file.write(qj)
        file.write(nl)
    if dc==11996:
        print(d7,"  ×4")
        qk=d7+"  ×4"
        file.write(qk)
        file.write(nl)
    if dc==14995:
        print(d7,"  ×5")
        ql=d7+"  ×5"
        file.write(ql)
        file.write(nl)
    if dc>14995:
        dc=14995
        print(d7,"  ×5")
        qz=d7+"  ×5"
        file.write(qz)
        file.write(nl)
        print("          :Stock is limited to 5 only")
        
              
#item E E E E E E E E E E E E E E E E E E E

    if ec==399:
        print(e7)
        file.write(e7)
        file.write(nl)
    if ec==798:
        print(e7,"  ×2")
        qx=e7+"  ×2"
        file.write(qx)
        file.write(nl)
    if ec==1197:
        print(e7, "  ×3")
        qc=e7+"  ×3"
        file.write(qc)
        file.write(nl)
    if ec==1596:
        print(e7,"  ×4")
        qv=e7+"  ×4"
        file.write(qv)
        file.write(nl)
    if ec==1995:
        print(e7,"  ×5")
        qb=e7+"  ×5"
        file.write(qb)
        file.write(nl)
    if ec>1995:
        ec=1995
        qn=e7+"  ×5"
        file.write(qn)
        file.write(nl)
        print(e7,"  ×5")
        print("          :Stock is limited to 5 only")          
                                                    
#item F F F F F F F F F    

    if fc==100:
        print(f7)
        file.write(f7)
        file.write(nl)
    if fc==200:
        print(f7,"  ×2")
        wq=f7+"  ×2"
        file.write(wq)
        file.write(nl)
    if fc==300:
        print(f7, "  ×3")
        ww=f7+"  ×3"
        file.write(ww)
        file.write(nl)
    if fc==400:
        print(f7,"  ×4")
        we=f7+"  ×4"
        file.write(we)
        file.write(nl)
    if fc==500:
        print(f7,"  ×5")
        wr=f7+"  ×5"
        file.write(wr)
        file.write(nl)
    if fc>500:
        fc=500
        print(f7,"  ×5")
        wt=f7+"  ×5"
        file.write(wt)
        file.write(nl)
        print("          :Stock is limited to 5 only")    
    
#item G G G G G G G G

    if gc==2999:
        print(g7)
        file.write(g7)
        file.write(nl)
    if gc==5998:
        print(g7,"  ×2")
        wy=g7+"  ×2"
        file.write(wy)
        file.write(nl)
    if gc==8997:
        print(g7, "  ×3")
        wu=g7+"  ×3"
        file.write(wu)
        file.write(nl)
    if gc==11996:
        print(g7,"  ×4")
        wi=g7+"  ×4"
        file.write(wi)
        file.write(nl)
    if gc==14995:
        print(g7,"  ×5")
        wo=g7+"  ×5"
        file.write(wo)
        file.write(nl)
    if gc>14995:
        gc=14995
        wp=g7+"  ×5"
        file.write(wp)
        file.write(nl)
        print(g7,"  ×5")
        print("          :Stock is limited to 5 only")        
    
#item H H H H H H H H H H H H H H H H 

    if hc==100:
        print(h7)
        file.write(h7)
        file.write(nl)
    if hc==200:
        print(h7,"  ×2")
        wa=h7+" ×2"
        file.write(wa)
        file.write(nl)
    if hc==300:
        print(h7, "  ×3")
        ws=h7+"  ×3"
        file.write(ws)
        file.write(nl)
    if hc==400:
        print(h7,"  ×4")
        wd=h7+"  ×4"
        file.write(wd)
        file.write(nl)
    if hc==500:
        print(h7,"  ×5")
        wf=h7+"  ×5"
        file.write(wf)
        file.write(nl)
    if hc>500:
        hc=500
        print(h7,"  ×5")
        wg=h7+"  ×5"
        file.write(wg)
        file.write(nl)
        print("          :Stock is limited to 5 only")        
    
#item I I I I I I 

    if ic==599:
        print(i7)
        file.write(i7)
        file.write(nl)
    if ic==1198:
        print(i7,"  ×2")
        wh=i7+"  ×2"
        file.write(wh)
        file.write(nl)
    if ic==1797:
        print(i7, "  ×3")
        wj=i7+"  ×3"
        file.write(wj)
        file.write(nl)
    if ic==2396:
        print(i7,"  ×4")
        wk=i7+"  ×4"
        file.write(wk)
        file.write(nl)
    if ic==2995:
        print(i7,"  ×5")
        wl=i7+"  ×5"
        file.write(wl)
        file.write(nl)
    if ic>2995:
        dc=2995
        print(i7,"  ×5")
        wz=i7+"  ×5"
        file.write(wz)
        file.write(nl)
        print("          :Stock is limited to 5 only")        
    
#item J J J J J J J J J J J J J J J J J J 

    if jc==199:
        print(j7)
        file.write(j7)
        file.write(nl)
    if jc==398:
        print(j7,"  ×2")
        wx=j7+"  ×2"
        file.write(wx)
        file.write(nl)
    if jc==597:
        print(j7, "  ×3")
        wc=j7+"  ×3"
        file.write(wc)
        file.write(nl)
    if jc==796:
        print(j7,"  ×4")
        wv=j7+"  ×4"
        file.write(wv)
        file.write(nl)
    if jc==995:
        print(j7,"  ×5")
        wb=j7+"  ×5"
        file.write(wb)
        file.write(nl)
    if jc>995:
        jc=995
        print(j7,"  ×5")
        wn=j7+"  ×5"
        file.write(wn)
        file.write(nl)
        print("          :Stock is limited to 5 only")        
    
    tc=ac+bc+cc+dc+ec+fc+gc+hc+ic+jc
    print("          ------------------------------------")
    print("\n          Total Price in INR     ", tc)
    print("          ------------------------------------\n")
    print("          Thank you for shopping...\n")
    print("          ------------------------------------")    
        
    
name( )                                
