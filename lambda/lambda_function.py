import json

def lambda_handler(event, context):

    # Extract the two numbers from the incoming JSON payload
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)

    # Calculate the sum
    total = num1 + num2

    # Return a clean JSON response
    return {
        'statusCode': 200,
        'Sum': total,
        'message': f'Cost Calculator: {num1} + {num2} = {total}'
    }
