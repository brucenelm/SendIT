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




if __name__ == "__main__":
	app.run(debug=True)