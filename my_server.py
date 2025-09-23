from flask import Flask, request, jsonify

def trial_division(n):
   if n == 1:
      return [1]
   factors = []
   while n % 2 == 0:
      factors.append(2)
      n //= 2
   p = 3
   while p * p <= n:
      while n % p == 0:
         factors.append(p)
         n //= p
      p += 2
   if n > 1:
      factors.append(n)
   return factors


app = Flask(__name__)

@app.route("/")
def hello():
   return " you called \n"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']


# Endpoint to factor an integer
@app.route("/factors", methods=['POST'])
def factors():
   try:
      in_int = int(request.form['inINT'])
   except (KeyError, ValueError):
      return jsonify({"error": "Missing or invalid inINT parameter"}), 400
   result = trial_division(in_int)
   return jsonify({"factors": result})

if __name__ == "__main__":
   app.run(host='0.0.0.0')