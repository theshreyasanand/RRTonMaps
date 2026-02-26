import numpy as np
import cv2
import matplotlib.pyplot as plt

def checkValid(x_1,y_1,x_2,y_2,image):
    mask = np.zeros_like(image, dtype=np.uint8)
    cv2.line(mask,(y_1,x_1),(y_2,x_2),255,1)
    linepixels=image[mask==255]
    return np.all(linepixels==0)

def closest(node_list, current):
    closest_dis=float('inf')
    index=-1
    for i in range(len(node_list)):
        x=node_list[i][0]
        y=node_list[i][1]
        dis=(x-current[0])**2+(y-current[1])**2
        if(dis<closest_dis):
            closest_dis=dis
            index=i
    return index,np.sqrt(closest_dis)

print("1)MAIN ENTRANCE")
print("2)LBS")
print("3)MAIN BUILDING")
print("4)CLOCK TOWER")
print("5)NALANDA CLASSROOM COMPLEX")
print("6)NEHRU MUSEUM")
print("7)GYMKHANA")
print("8)TATA STEEL SPORTS COMPLEX")
print("9)SNVH")
print("10)BC ROY HOSPITAL")
print("11)TECH MARKET")
print("Enter the Start and Destination Serial Number:-")
coordinates=[[58,721],[130,297],[187,692],[297,600],[239,1042],[203,936],[207,419],[298,641],[318,490],[310,343],[353,334]]

start=coordinates[int(input())-1]
end=coordinates[int(input())-1]
img=cv2.imread(r"Map of IIT KGP.png",cv2.IMREAD_GRAYSCALE)
img2=cv2.imread(r"Map of IIT KGP.png")
for p in range(0,img.shape[0]):
    for q in range(0,img.shape[1]):
        if img[p,q]<200:
            img[p,q]=255
        else:
            img[p,q]=0
node_list=[start]
parent_node=[0]
threshold=7
cv2.ellipse(img2,(end[1],end[0]),(5,5),0,0,360,(0,0,255),-1)
cv2.ellipse(img2,(start[1],start[0]),(5,5),0,0,360,(255,0,0),-1)
while True:
    x,y=np.random.randint(0,img.shape[0]),np.random.randint(0,img.shape[1])
    if(img[x,y]!=0):
        continue
    ind,distance=closest(node_list,[x,y])
    
    if(distance>threshold):
        x2,y2=node_list[ind]
        angle = np.arctan2(y - y2, x - x2)
        x = round(threshold * np.cos(angle)) + x2
        y = round(threshold * np.sin(angle)) + y2

    if(checkValid(node_list[ind][0],node_list[ind][1],x,y,img)):
        cv2.ellipse(img2,(y,x),(1,1),0,0,360,(0,255,0),-1)
        node_list.append([x,y])
        parent_node.append(ind)
        cv2.line(img2,(node_list[ind][1],node_list[ind][0]),(y,x),(0,255,0),2)
        cv2.line(img,(node_list[ind][1],node_list[ind][0]),(y,x),(255),1)
        img[x,y]=0
        img[node_list[ind][0],node_list[ind][1]]=0
        cv2.imshow("RRT IMPLEMENTATION",img2)
        cv2.waitKey(1)
        if(np.sqrt((y-end[1])**2+(x-end[0])**2)<=15):
            node_list.append(end)
            parent_node.append(len(node_list)-2)
            break
current=node_list[len(node_list)-1] 
while(True):
    xnode,ynode=node_list[parent_node[node_list.index(current)]]
    cv2.line(img2,(ynode,xnode),(current[1],current[0]),(255,0,0),3)
    cv2.imshow("RRT IMPLEMENTATION",img2)
    cv2.waitKey(100)
    if(parent_node[node_list.index(current)]==0):
        break
    current=[xnode,ynode]        
cv2.ellipse(img2,(end[1],end[0]),(5,5),0,0,360,(0,0,255),-1)
cv2.ellipse(img2,(start[1],start[0]),(5,5),0,0,360,(255,0,0),-1)
cv2.imshow("RRT IMPLEMENTATION",img2)
cv2.waitKey(0)
