from flask import Flask, render_template, jsonify
 
 
def page_not_found(e):
  return jsonify(server_name="flask_server", error=str(e)), 404
 
 
app = Flask(__name__)
app.register_error_handler(404, page_not_found)
 
 
@app.route('/')
def hello_world():
    return 'Hello, World!'
 
 
@app.route('/publish')
def hello_publish():
    return 'Hello, this is publish!'
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False, port=8080)
    