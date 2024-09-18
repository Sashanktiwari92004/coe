def chatbot_response(input_user):
    response = {
        "hii": "hello! how are you",
        "bye": "bye sir have a nice day",
        "what are you you doing": "nothing tell about yourself"
    }

    for key in response.keys():
        if key in input_user.lower():
            return response[key]
    return "sorry, i don't understand."

while True:
    input_user = input("you: ")
    if input_user.lower() == "exit":
        break
    print("chatbot:", chatbot_response(input_user))