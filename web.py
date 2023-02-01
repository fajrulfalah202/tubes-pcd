
from flask import Flask, render_template, request, flash, redirect
from fileinput import filename
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from werkzeug.utils import secure_filename
import os
import cv2
import base64
import io


app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config["SIMPAN_GAMBAR"]=r"C:\Users\FAJRUL FALAH\Documents\kuliyah\semester 3\citra digital\penajaman citra web\upload"



@app.route('/')
def home():
 return render_template("awal.html")


@app.route('/succsess', methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        if request.files:
            file = request.files['mentah']
           
        if file :

            file.save(os.path.join(app.config["SIMPAN_GAMBAR"], file.filename))
            print("data terupload")
       
        
        n= 1
        path ="C:/Users/FAJRUL FALAH/Documents/kuliyah/semester 3/citra digital/penajaman citra web/upload/"
        daftar = os.listdir(path)
        for filename in daftar:
            alamat = path + filename
            des = "target"+ str(n)+".png"
            if not os.path.exists(des):
                os.rename(alamat, des)
                n =+1

        imeg = cv2.imread('target1.png')
        #cv2.imwrite('static/sebelum.png', imeg)
        blur = cv2.medianBlur(imeg, 5)
        #cv2.imwrite('static/simpan.png', blur)
        file_object = io.BytesIO()
        img= Image.fromarray(blur)
        img.save(file_object, 'PNG')
        base64img = "data:image/png;base64,"+base64.b64encode(file_object.getvalue()).decode('ascii')
       
        return render_template("sukses.html", imagee=base64img)
       
      
@app.route('/ulang', methods=["GET", "POST"]) 
def back():
    if request.method == 'POST':
       os.remove("target1.png") 
    return render_template("awal.html")


        
        

def allowed_file(filename):
    return  '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS






    
if __name__ == '__main__':
    app.run(debug= True)