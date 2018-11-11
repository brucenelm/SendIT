from flask import Flask, request, request, jsonify

app = Flask(__name__)

# list of deliveries with some default data
list_of_all_deliveries =[
	{'userid':'alice','parcelid':1,'item_name':'Led Screan', 'canceled': 0},
	{'userid':'tom','parcelid':2,'item_name': 'Laptop Batteries', 'canceled': 0},
	{'userid':'tom','parcelid':3,'item_name':'Laptop', 'canceled': 0}
]

#Fetch all Parcel delivery orders
@app.route('/<version>/parcels', methods = ['GET'])
def allParcelDeliveredOrders(version):
	return jsonify({'data':list_of_all_deliveries})

#Fetches a specific parcel delivery order
@app.route('/<version>/parcels/<int:parcelid>', methods = ['GET'])
def getDelivereParcel(version, parcelid):
	try:
		parcel = list_of_all_deliveries[parcelid-1]
	except IndexError:
		return jsonify({'error':'Parcel not found'}), 404
	return jsonify({'data':parcel})

#fetch all parcel delivery orders by a specific user
@app.route('/<version>/users/<userid>/parcels', methods = ['GET'])
def getDeliveryParcelPerUser(version, userid):
	parcel = [parcels for parcels in list_of_all_deliveries if parcels['userid']==userid]
	return jsonify({'data':parcel[0]})

#Cancel the specific parcel delivery order
@app.route('/<version>/parcels/<int:parcelid>/cancel', methods = ['PUT'])
def cancelDelivereParcel(version, parcelid):
	try:
		list_of_all_deliveries[parcelid-1]['canceled'] = 1
	except IndexError:
		return jsonify({'error':'Parcel not found'}), 404

	return jsonify({'data':list_of_all_deliveries})



if __name__ == "__main__":
	app.run(debug=True)