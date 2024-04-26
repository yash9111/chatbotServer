from flask import Flask ,request,jsonify
import pickle
from gemini import chat_with_gemini

app = Flask('__main__')



app.route('/chatwithbot',method=['POST'])
def chat_with_bot():
    
    prompt_part = request.data
    gemini_responce= chat_with_gemini(prompt_part)
    
    return jsonify(gemini_responce.text)

if __name__ == '__main__':
    app.run(debug=True)