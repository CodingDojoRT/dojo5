import unittest
import smallWorld

Miguxo = smallWorld.Miguxo
SW = smallWorld.SmallWorld

migs1 = Miguxo(1, [10, 10])
migs2 = Miguxo(2, [13, 14])
migs3 = Miguxo(3, [15, 10])
migs4 = Miguxo(4, [20, 20])
migs5 = Miguxo(5, [12, 12])

migsList = [migs1, migs2, migs3, migs4, migs5]

class Test(unittest.TestCase):
	def testNearbyFriends(self):
		expectedResult = [migs5, migs2, migs3]
		testMigList = migsList[1:]
		result = SW.friendsNearbyThis(migs1, testMigList)
		self.assertEqual(result, expectedResult)

	def testCalculateDistance(self):
		p1 = [10,10]
		p2 = [13,14]
		print sorted({10: 'a', 12: 'b', 9: 'c'})		
		self.assertEqual(SW.calculateDistance(p1,p2),5)

	def testSmallWord(self):
		mig1 = Miguxo(1, [10, 10])
		mig2 = Miguxo(2, [10, 11])
		mig3 = Miguxo(3, [10, 12])
		mig4 = Miguxo(4, [10, 14])
		mig5 = Miguxo(5, [10, 15])		

		migList = [mig1, mig2, mig3, mig4, mig5]		

		xpekeList = [ [mig2, mig3, mig4], [mig1, mig3, mig4], [mig2, mig1, mig4], [mig5, mig3, mig2], [mig4, mig3, mig2]]
		self.assertEqual(xpekeList,SW.AllFriendsNearby(migList))
		