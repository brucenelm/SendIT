import unittest
import run
import json
from flask_testing import TestCase
# from .run import app

class TestMainFlask(TestCase):

	def create_app(self):
		return run.app

	#tests if the nomber of elements in the list is more than zero
	def test_get_all_parcels(self):
		response = self.client.get('v1/parcels')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(len(data['data']),0)

	#tests that the record with parcelid 1 is returned

	def test_get_one_parcel(self):
		response = self.client.get('v1/parcels/1')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['data'],{'userid':'alice','parcelid':1,'item_name':'Led Screan','canceled':0})

	#tests that a specified record is returned
	def test_get_one_parcel_per_user(self):
		response = self.client.get('v1/users/alice/parcels')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['data'],{'userid':'alice','parcelid':1,'item_name':'Led Screan','canceled':0})

	

if __name__ == '__main__':
	unittest.main()