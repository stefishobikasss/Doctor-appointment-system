import mysql.connector as ms
db=ms.connect(host="localhost",user="root",password="stefi",database="docappo")
a=db.cursor()

def clear():
    for _ in range(2):
        print()

def add():#TO ADD AN APPOINTMENT
    try:
        f=int(input("ENTER PATIENT ID:"))
        b=input("PATIENT NAME:")
        c=input("DOCTOR NAME:")
        d=input("REASON:")
        e=input("TIME:")
        q1="insert into patient_details (patient_id,patient_name,doctor_name,reason,appointment_time)values (%s,%s,%s,%s,%s)"
        val=(f,b,c,d,e)
        a.execute(q1,val)
        db.commit()
        print("DONE")
    except:
        print("SOMETHING IS WENT WRONG!")

def remove():#PATIENT CANCELLING THE APPOINTMENT
    try:
        b=input("ENTER PATIENT NUM:")
        c=("delete from patient_details where patient_id=%S",(b,))
        print("THE APPOINTMENT HAS BEEN CANCELLED")
        db.commit()
        return
    except:
        print("YOU DID NOT BOOK ANY APPOINTMENTS WITH US")
def update():
    try:
        acd=input("ENTER THE TIME YOU HAVE BOOKED:")
        bcd=input("ENTER THE TIME YOU WANNA CHANGE:")
        record=a.fetchall()
        for x in record:
            if x[4]==bcd:
                print("THE SLOT HAS BEEN BOOKED ALREADY PICK ANOTHER SLOT!")
            else:
                q1="update patient_details time=%s where patient_id=%s"
                val=(bcd,acd)
                a.execute(q1,val)
                db.commit()
        print("DONE")
        return
    except:
        print("SOMETHING WENT WRONG!")

ch="y"
while ch=="y":
    clear()
    print("="*105)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ABC HOSPITAL APPOINTMENT BOOKING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("="*105)
    print("1.TO BOOK THE APPOINTMENT")
    print("2.TO CANCEL THE APPOINTMENT")
    print("3.TO UPDATE THE TIMINGS")
    choice=int(input("ENTER YOUR CHOICE (1..3):"))
    if choice==1:
        add()
    if choice==2:
        remove()
    if choice==3:
        update()
        


    ch=input("do you wanna continue (y/n)?:")
db.close()
        
