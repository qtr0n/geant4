if np.logical_and(x**2 + y**2 <= R**2, abs(z)<H/2):
	dens=10
else:
	dens=0.001

mfp = 1.0/(sigTot*dens)

length=randomExpo(mfp)

if randomPhotOrComp(sigComp,sigPhot):
	scatTheta=0.0
	scatPhi=0.0
	nextE=0.0
else:
	scatTheta=rejectionRandom_compDir(E)
	scatPhi=randomPhi()
	nextE=nextE_compton(E,scatTheta)

nextR=r + length*phat
nextP = nextE/c*scatterDir(phat,scatTheta,scatPhi)

def randomInitial(P):
	phi=np.random.uniform(0,2*pi);
	Z=np.random.uniform()
	theta=arccos(1-2*Z);
	return [0,0,0,P*sin(theta)*cos(phi),P*sin(theta)*sin(phi),P*cos(theta)]

x0=randomInitial(P)
track[x0]

while True:
	s=simStep(x0,radius)
	R=radius
	H=2.0
	track.append(s)
	x0=s
	x,y,z=x0[0:3]
	if norm(x0[3:6]<1.0e-3 or x**2+ y**2 > R**2 or abs(z)>H/2):
		return np.array(track)

escV=np.vectorize(esc)	

def rad(P,radius,i):
	escP=np.zeros(i)
	for i in range(i):
		escP[i]=escV(P,radius)
	return escP,sum()

f.plot_wireframe(X,Y,Z)
f.plot_wireframe(X,-Y,Z)