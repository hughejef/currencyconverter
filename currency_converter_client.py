import zmq

def send_request(source_currency, target_currency):
    '''
    sends request to server side
    '''
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5353")
    
    # dictionary message with source and targe currencies:
    message = {
        'sourceCurrency': source_currency,
        'targetCurrency': target_currency
    }
    print(message)
    # send message as JSON
    socket.send_json(message)
    
    # receive server response
    response = socket.recv_json()
    print(response)
    return response


# :::::::: TEST PROGRAM ::::::::


# supported Currency Examples = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']

if __name__ == '__main__':

    
    while True:
        
        source_currency = input("Enter the source currency: ").upper()
        
        target_currency = input("Enter the target currency: ").upper()
        
        response = send_request(source_currency, target_currency)
        data = response['serverResponse']
        
        print(f"1 {data['sourceCurrency']} is equal to {data['convertedAmount']} {data['targetCurrency']}")
