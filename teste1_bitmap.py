# Importing dependencies.

import numpy as np
from flask import Flask, jsonify, request

# Setup Flask, prevent jsonify from alphabetically sorting my keys
# because I want them sorted numerically.

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])
def index():
	return jsonify({"about": "Hello! To set up your matrix for testing, add the following to your URL, replacing INT with an integer of your choice: /test/?nx=INT&ny=INT"})

# Setup GET method to allow the user to input the size of the
# matrix that's gonna be tested.

@app.route('/test/', methods=['GET'])
def get_matrix():

	# Setup requests to allow the user to input the size of the randomly
	# generated matrix.

	nx = int(request.args.get('nx'))
	ny = int(request.args.get('ny'))
	x, y = (0, 0)
	bmp = np.random.random_integers(0,15, size=(nx,ny))
	arr = np.array([0, 1, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 11, 12, 13, 14, 15])
	qty = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

	def check_number(nb, arr, qty):
		for x in arr:
			if arr[x] == nb:
				qty[nb] += 1
		return qty

	for row in bmp:
		print(row)

	for x in range(nx):
		y = 0
		for y in range(ny):
			qty = check_number(bmp[x][y], arr, qty)
			y += 1
		x += 1

	#jsonify cannot read numpy arrays, so I'm converting it to a regular list.

	new = qty.tolist() 
	return jsonify({'0': new[0], '1': new[1], '2': new[2], '3': new[3], '4': new[4], '5': new[5], '6': new[6],
	'7': new[7], '8': new[8], '9': new[9], '10': new[10], '11': new[11], '12': new[12], '13': new[13],
	'14': new[14], '15': new[15]})

if __name__ == '__main__':
	app.run(debug=True)