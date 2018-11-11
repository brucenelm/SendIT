import unittest
import run
import json
from flask_testing import TestCase
# from .run import app

class TestMainFlask(TestCase):

	def create_app(self):
		return run.app

	def test_get_all_parcels(self):
		response = self.client.get('v1/parcels')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(len(data['data']),0)

	def test_get_one_parcel(self):
		response = self.client.get('v1/parcels/1')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['data'],{'userid':'alice','parcelid':1,'item_name':'Led Screan','canceled':0})


	def test_get_one_parcel_per_user(self):
		response = self.client.get('v1/users/alice/parcels')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['data'],{'userid':'alice','parcelid':1,'item_name':'Led Screan','canceled':0})

	def test_to_cancel_one_parcel(self):
		self.client.put('v1/parcels/1/cancel')
		response = self.client.get('v1/parcels/1')

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 200)
		self.assertEqual(data['data'],{'userid':'alice','parcelid':1,'item_name':'Led Screan','canceled':1})

	def test_create_one_parcel(self):
		#response = self.client.post('v1/parcels')
		response = self.client.post('v1/parcels',
                                        content_type='application/json',
                                        data=json.dumps(dict(userid='bob',name='Books')))

		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 201)
		self.assertEqual(data['data'],{'userid':'bob','parcelid':4,'item_name':'Books','canceled':0})

if __name__ == '__main__':
	unittest.main()