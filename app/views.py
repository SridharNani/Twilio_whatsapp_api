# # from http.client import HTTPResponse
# # from django.shortcuts import render
# # from twilio.rest import Client
# # from django.views.decorators.csrf import csrf_exempt

# # # Create your views here.
# # account_sid = 'AC6489af9797220c83c7a4a8abdc5b8226'
# # auth_token = 'b936b0f1eef07fb5c238cca412275d02'
# # client = Client(account_sid, auth_token)


# # @csrf_exempt
# # def bot(request):
# #     # message=request.POST["message"]
# #     print(request.POST)
# #     # if message=="hi":
# #     #     client.messages.create(
# #     #                 from_='whatsapp:+14155238886.',
# #     #                 body='Hello from Python!',
# #     #                 to='whatsapp:+918143510050'
# #     #                 )
                    
# #     return HTTPResponse("Hello")                

# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)



# @app.route('/',methods = ['POST', 'GET'])
# def login():
# #    if request.method == 'POST':
# #       user = request.form['nm']
# #       return redirect(url_for('success',name = user))
# #    else:
# #       user = request.args.get('nm')
#       return ("Hello")

# if __name__ == '__main__':
#    app.run(debug = True)