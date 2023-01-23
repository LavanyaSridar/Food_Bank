from django.shortcuts import render
import mysql.connector as sql
import messagebox

def coupon(request):
    Name=''
    contactno=''
    Email_id=''
    Course=''
    Preferences=''
    Restaurants=''
    Food_required=''
    
    if (request.method=="POST"):
        food=sql.connect(host="localhost",user="root",password="admin",database="canada")
        cursor=food.cursor()
        e=request.POST
        for key,value in e.items():
            if key=="Name":
                Name=value
            if key=="contactno":
                contactno=value
            if key=="Email_id":
                Email_id=value
            if key=="Course":
                Course=value
            if key=="Preferences":
                Preferences=value
            if key=="Restaurants":
                Restaurants=value
            if key=="Food_required":
                Food_required=value
            
        c="insert into downtown values('"+Name+"','"+contactno+"','"+Email_id+"','"+Course+"','"+Preferences+"','"+Restaurants+"','"+Food_required+"')"

        cursor.execute(c)
        food.commit()
        food.close()
        messagebox.showinfo("successfull","Thanks")
        
    return render(request,"Foodcoupon.html")
