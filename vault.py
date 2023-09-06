from tkinter import *
from tkinter import messagebox

def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if len(website)==0 or len(password)==0:
        messagebox.showerror(title="Ooops",message="Don't Leave any field Empty!")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"You have Entered\nEmail: {email}\nPassword: {password}\n"f"Are You Sure to Save?")
        if is_ok:
            with open("data.txt","a")as f:
                f.write(f"Your Application Name or Website:{website} |E-mail: {email} |Password: {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                email_entry.delete(0,END)
                
def show():
    if password_entry.cget('show')=='*':
        password_entry.config(show='')
    else:
        password_entry.config(show='*')    
                        
root=Tk()
root.title("Password Vault")
root.geometry("800x600")
root.resizable(0,0)
root.config(padx=50,pady=50,background="skyblue")
# canvas=Canvas(width=100,height=100)
# photo=PhotoImage(file="icons8-lock-50.png")
# canvas.create_image(50,50,image=photo,)
# canvas.grid(column=1,row=0)
img=PhotoImage(file="output-onlinepngtools.png")
label_img=Label(root,image=img,background="skyblue")
label_img.grid(column=1,row=0)

label=Label(root,text="Password Vault",font=("Imprint MT shadow",25),background="skyblue")
label.grid(column=1,row=1,pady=10)

website=Label(text="Application Name or Website : ",background="skyblue",font=("cambria",13))
website.grid(column=0,row=2,pady=5,padx=5)
email=Label(text="Email/Username : ",background="skyblue",font=("cambria",13))
email.grid(column=0,row=3,pady=5,padx=50)
password=Label(text="Password : ",background="skyblue",font=("cambria",13))
password.grid(column=0,row=4,pady=5,padx=50)

website_entry=Entry(width=28,font=("arial",15),bd=2,highlightcolor="Blue",highlightthickness=2)
website_entry.grid(column=1,row=2,columnspan=2,pady=5)
email_entry=Entry(width=28,font=("arial",15),bd=2,highlightcolor="Blue",highlightthickness=2)
email_entry.grid(column=1,row=3,columnspan=2,pady=5)
#email_entry.insert(0,"baghelsatendra@gmail.com")
password_entry=Entry(width=22,show='*',font=("arial",15),bd=2,highlightcolor="Blue",highlightthickness=2)
password_entry.grid(column=1,row=4,pady=5)


generate_btn=Button(text="Show",command=show,activebackground="green",bd=3,highlightcolor="Blue",highlightthickness=2)
generate_btn.grid(column=2,row=4,pady=5)
add_btn=Button(text="Add",width=36,command=save,background="lightgreen",font=("arial",10),activebackground="lightblue",bd=3)
add_btn.grid(column=1,row=5,columnspan=2,pady=15)

purpose=Label(root,text="Purpose : Password Vault allows users to create unique,\n complex passwords for every online account without needing to remember them.",background="skyblue",fg="red",font=("Bell MT",13))
purpose.grid(columnspan=4)

root.mainloop()