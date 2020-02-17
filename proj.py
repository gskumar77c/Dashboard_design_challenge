from flask import Flask,render_template,flash,redirect,url_for,request,send_from_directory
import os

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def index():
    return render_template('screenshot.html',)


@app.route('/image/<filename>')
def send_image(filename):
    #print(filename)
    return send_from_directory("image", filename)


@app.route('/images')
def show_images():
    image_names = os.listdir('./image')
    
    gsk = []
    for name in image_names:
        nm = name.replace('.','_');
        nm = list(nm.split('_'));
        gsk.append({'imagename':name, 'min':nm[1] , 'sec' : nm[2]});
    return render_template("images.html", image_names=gsk)


if __name__ == '__main__':
    
    app.run(debug = True)
