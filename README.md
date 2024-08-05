Instructions to REQUEST:

To make a REQUEST to the ZeroMQ server, the client needs to send a message (formatted as a JSON) containing a dictionary with source_currency and a target_currency as key values to the server. 
Example:   
To request convert_currency:
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5353")
    message = {'sourceCurrency': 'USD', 'targetCurrency': 'EUR'}
    socket.send_json(message)

Instructions to RECEIVE:

In order to receive the data, the user should assign a variable to the recv_json() function associated with the socket declared in the request call. 

Example:
response = socket.recv_json()

A dictionary is returned in the response so assigning a variable allows you to use standard dictionary index functions on the response.

An example of what the response looks like is:
{'ServerResponse': {'sourceCurrency': 'USD', 'targetCurrency': 'JPY', 'convertedAmount': 147.51}}

So you can return the converted amount of the target currency by referencing the key value in the dictionary:

convertedAmountReceived = ServerResponse[‘response’][‘convertedAmount’]
 
![image](https://github.com/user-attachments/assets/bb852928-4ab6-4805-b172-f10af1fa9fdb)
