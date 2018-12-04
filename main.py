from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form  action="/" method="post">
        <label for="Caesar Cypher">
            Rotate by:  
            <input type="text" id="rot" name="rot" value ="0"/ ><br><br>
            <textarea id="text" name="text">{0}</textarea><br><br>
        </label>       
        <input type="submit" value="Submit Cypher"/>
    </form>
    
    </body>
</html>"""

@app.route("/", methods=['POST'])
def encrypt():
    loc_rot = int(request.form['rot'])
    loc_text = request.form['text']
    output = rotate_string(loc_text, loc_rot)
    output_html = "<h1>" + output + "</h1>"

    return form.format(output)


@app.route("/")
def index():
    return form.format(form)

app.run()
