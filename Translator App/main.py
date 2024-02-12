from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob
from PIL import ImageTk, Image


root=Tk()
root.title("GOOGLE TRANSLATOR")
root.geometry("1080x400")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now(again=None):
    global language
    try:
        text=text1.get(1.0, END)
        c2 = combo1.get()
        c3 = combo2.get()
        if (text):
            words = textblob.TextBlob(text)
            lan = words.detect_language()
            for i, j in language.items():
                if (j == c3):
                    lan_ = i
            words = words.translate(from_lang=lan, to=str(lan_))
            text2.delete(1.0, END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror("googletrans", "Lütfen tekrar deneyin")


#icon
# Add image file
bg = PhotoImage(file="background.png")

#arrow
arrow_image=PhotoImage(file="arrow.png")
image_label=Label(root,image=arrow_image,width=150)
image_label.place(x=460,y=50)


# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

language = googletrans.LANGUAGES
languageA = list(language.keys())
lang1 = languageA

combo1=ttk.Combobox(root,values=languageA,font="Montserrat 14",state="r")
combo1.place(x=100,y=20)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1=Text(f,font="Montserrat 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


combo2=ttk.Combobox(root,values=languageA,font="Montserrat 14",state="r")
combo2.place(x=730,y=20)
combo2.set("Select Language")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1=Frame(root,bg="Black",bd=5)
f1.place(x=620,y=118,width=440,height=210)

text2=Text(f1,font="Montserrat 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text1.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translate button
translate=Button(root,text="Translate",font="Montserrat 15 bold italic",activebackground="red",cursor="hand1",bd=5,bg="red",fg="white",command=translate_now)
translate.place(x=480,y=250)




label_change()

root.configure(bg="white")
root.mainloop()