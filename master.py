# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import sqlite3, base64, hashlib, binascii

app = Flask(__name__)
    
@app.route("/authenticate", methods = ['POST'])
def authenticate():
    if request.method == "POST":
        #req = request.get_json(cache=False)
        print(request.headers)
        if "Authorization" in request.headers:
            creds = request.headers["Authorization"]
            
            if "Basic " in creds:
                creds = creds.strip()
                try:
                    creds = base64.b64decode(creds[creds.index(" ") + 1 :]).decode('UTF-8')
                except binascii.Error:
                    print("Error when decoding credentials")
                    return "", 403
                
                username = creds[: creds.index(":")]
                print("username : "+username)
                password = creds[creds.index(":") + 1:]
                password = hashlib.sha3_512(password.encode()).hexdigest()
                print("password : " + password)
            con = sqlite3.connect('hcore.db')
            cur = con.cursor()
            cur.execute("SELECT id FROM users WHERE username='" + username + "' AND password='" + password + "'")
            result = cur.fetchone()
            cur.close()
            if result != None:
                return jsonify({'id': str(result[0])}), 202
        
        return "", 403
        
        
if __name__ == "__main__":
    app.run(debug=True, port=8001)