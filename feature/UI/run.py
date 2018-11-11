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




if __name__ == "__main__":
	app.run(debug=True)