import math

class Miguxo(object):
	def __init__(self, aidi, pos):
		self.aidi = aidi
		self.pos = pos
	def __repr__(self):
		return str(self.pos)
	def __str__(self):
		return self.__repr__()

class SmallWorld(object):
	@staticmethod
	def calculateDistance(p1,p2):
		return (((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))**0.5

	@staticmethod
	def friendsNearbyThis(friend, otherFriends):
		greatestDistance = 0
		return sorted(otherFriends, key=lambda f: SmallWorld.calculateDistance(friend.pos, f.pos))[:3]


	@staticmethod
	def AllFriendsNearby(friends):
		listafinal = []
		for x in friends:
			def idIguau(mig):
				return mig.aidi != x.aidi 
			listadaora = filter(idIguau,friends)
			print 'wababababababa'
			print 'eu sou esse cara ' + str(x)
			listafinal.append(SmallWorld.friendsNearbyThis(x, listadaora))
		return listafinal