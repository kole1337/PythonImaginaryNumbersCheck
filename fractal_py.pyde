background(0)
size(2000,2000)

f=open("coordinates.txt","r")
l=f.readline()
l=l.strip()
l=l.split(":")
l2=0




iter = 0

for num in range(3,50):
    with open("iter"+str(num)+".txt","r") as iter:
        l2=iter.readline()
        for l2 in iter:
            l2=l2.strip()
            l2=l2.split(":")
            y2=(float(l2[0]))*500
            x2=(float(l2[1])*-1)*500
            stroke(114+num, 230, 255, 0+(5*num))
            smooth()
            point(x2+1000,y2+1300)
with open("coordinates.txt","r") as f:
    for l in f:
        l=l.strip()
        l=l.split(":")
        y=(float(l[0]))*500
        x=(float(l[1])*-1)*500
        stroke(0,0,0,255)
        smooth()
        point(x+1000,y+1300)
        
with open("coordinates.txt","r") as f:
    for l in f:
        l=l.strip()
        l=l.split(":")
        y=(float(l[0]))*500
        x=(float(l[1])*-1)*500
        stroke(0,0,0,255)
        smooth()
        point(x+1000,y+1300)
        
#filter(BLUR, 0.55)
save("Mandlebrot.png")
        
