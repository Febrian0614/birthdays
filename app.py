#import os untuk mengakses sistem database
import os

#import SQL untuk menggunakan bahasa SQL dalam python
from cs50 import SQL
#import tools untuk website
from flask import Flask,flash,jsonify,redirect,render_template,request,session

#mengatur nama aplikasi
app = Flask(__name__)

#dipakai untuk koneksi ke database
db = SQL("sqlite:///birthdays.db")

#https://127.0.0.1:5000/
@app.route("/",methods=["GET", "POST"])
#ketika route "/" dipangil/diakses, maka fungsi index() dieksekusi
def index():
    #jika request yang dilakukan oleh penguna adalah post,maka eksekusi kode dalam if
    if request.method == "POST":

    #Acces from data/ membaca data yang diisikan pada from
        name = request.form.get("name") #ambil data dari input name
        month = request.form.get("month")#ambil data dari input month
        day= request.form.get("day")#ambil data dari input day

    #insert data into database, masukan data name, month, day ke database
        db.execute("INSERT INTO brithdays (name, month, day) VALUES(?, ?, ?)",name, month, day)

    #balik ke https://127.0.0.1:5000/
        return redirect("/")

    else:

        #ambil seluruh data dari tabel birthdays, simpan di variabel birthdays
        brithdays = db.execute("SELECT* FROM brithdays")

        #salin isi variabel ke brithdays,lalu kirim ke index.html
        return render_template("index.html", brithdays=brithdays)