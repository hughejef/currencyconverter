import zmq
import requests




def convert_currency(source_currency, target_currency):
    '''
    Takes as parameters a source currency and returns the conversion rate for 1 unit of source
    currency to the target currency. 
    '''
    source_currency = source_currency.upper() # format all upper case
    target_currency = target_currency.upper()

    # API URL to get exchange rates
    api = f'https://api.exchangerate-api.com/v4/latest/{source_currency}'
    
    try:
        response = requests.get(api)
        rates = response.json().get('rates') # pull rates from API
                
        converted_target = rates[target_currency]

        result = {
            'sourceCurrency': source_currency,
            'targetCurrency': target_currency,
            'convertedAmount': converted_target
        }

        return result
    
    except Exception as program_error:
        return {'error': str(program_error)}




if __name__ == "__main__":
        
    # establish the ZeroMQ server. 
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5353")

    # wait for request from client
    while True:
        message = socket.recv_json()
        source_currency = message.get('sourceCurrency')
        target_currency = message.get('targetCurrency')
        
        # return conversion
        response = convert_currency(source_currency, target_currency)
        socket.send_json({'serverResponse': response})
