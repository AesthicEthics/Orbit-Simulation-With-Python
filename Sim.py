def orbit(x,y,vx,vy,t_s,Mb):
	#import packages
	import numpy as np
	#get polar coordinates
	r = np.sqrt(np.abs(x)**2+np.abs(y)**2)
	theta = np.arctan2(y,x)
	a = -G*Mb/(r**2)
	#lets do some kinematics
	ax = a*np.cos(theta)
	ay = a*np.sin(theta)
	vx = vx + ax*t_s
	vy = vy + ay*t_s
	x = x + vx*t_s + 0.5*ax*t_s**2
	y = y + vy*t_s + 0.5*ay*t_s**2
	#print(theta)
	return(x,y,vx,vy)


def creategif(filename,step):
	import imageio
	from pygifsicle import optimize
	gif_path =    "12video"+str(".gif")
	frames_path = str(filename)+str("{w}.png")

	with imageio.get_writer(gif_path, mode='I') as writer:
		for w in range(step+1):
			writer.append_data(imageio.imread(frames_path.format(w=w)))	
	
  
  #define  constants
M_e = 5.972 * 10**24 #kg
M_m = 7.34767309 * 10**22 #kg
G   =  6.67408 * 10**-11 #m^3 kg^-1 s^-2
#import packages
import numpy as np
import matplotlib.pyplot as plt

#initial conditions
d_orbit= 384400000   #m
period = 27*24*3600 #day*hrs/day*secs/hour = secs
t_s = 3600*12 #sec

for t in range(0,int(period),t_s):
	#set initial conditions
	if t==0:
		x=d_orbit
		y=0
		vx=0
		vy=1019
		#vy=d_orbit*2*np.pi/period
	else:
		x,y,vx,vy = orbit(x,y,vx,vy,t_s,M_e)
    
	plt.scatter(0,0,s=100)
	plt.scatter(x,y,s=20)
	plt.xlabel("x distance (m)")
	plt.ylabel("y distance (m)")
	plt.xlim(-d_orbit-0.1*d_orbit,d_orbit+0.1*d_orbit)
	plt.ylim(-d_orbit-0.1*d_orbit,d_orbit+0.1*d_orbit)
	plt.title("Moon orbiting Earth at time = "+str(t/3600)+" hours")
	step = int(t/t_s)
	print(step)
	filename = "s_"
	plt.savefig(filename+str(step)+str(".png"), format='png',bbox_inches='tight') 
	plt.close()
creategif(filename,step)
