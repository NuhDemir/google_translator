from tkinter import *  # Import Tkinter for GUI elements
from tkinter import ttk, messagebox  # Import ttk for themed widgets and messagebox for dialogs
import googletrans  # Import Google Translate library
import textblob  # Import TextBlob for text analysis and translation
from PIL import ImageTk, Image  # Import ImageTk for handling images

# --- Main application window ---
root = Tk()  # Create the main window
root.title("GOOGLE TRANSLATOR")  # Set the window title
root.geometry("1080x400")  # Set the window size

# --- Function to update labels ---
def label_change():
    c = combo1.get()  # Get the selected value from combo1
    c1 = combo2.get()  # Get the selected value from combo2
    label1.configure(text=c)  # Update the text of label1
    label2.configure(text=c1)  # Update the text of label2
    root.after(1000, label_change)  # Call this function again after 1 second

# --- Function to translate text ---
def translate_now(again=None):
    global language  # Access the global language dictionary
    try:
        text = text1.get(1.0, END)  # Get the text to be translated
        c2 = combo1.get()  # Get the selected value from combo1
        c3 = combo2.get()  # Get the selected value from combo2
        if text:  # Check if there's text to translate
            words = textblob.TextBlob(text)  # Create a TextBlob object
            lan = words.detect_language()  # Detect the language of the text
            for i, j in language.items():  # Find the language code for the target language
                if j == c3:
                    lan_ = i
            words = words.translate(from_lang=lan, to=str(lan_))  # Translate the text
            text2.delete(1.0, END)  # Clear the output text box
            text2.insert(END, words)  # Insert the translated text
    except Exception as e:  # Handle any exceptions
        messagebox.showerror("googletrans", "Lütfen tekrar deneyin")  # Show an error message

# --- Load background image and create label ---
bg_image = PhotoImage(file="background.png")  # Load the background image
background_label = Label(root, image=bg_image)  # Create a label for the background
background_label.place(x=0, y=0)  # Position the background image

# Load the arrow image and display it as a label
arrow_image = PhotoImage(file="arrow.png")
arrow_label = Label(root, image=arrow_image, width=150)
arrow_label.place(x=460, y=50)

# Create a background label using a white background color
label1 = Label(root, bg="white")
label1.place(x=0, y=0)

language = googletrans.LANGUAGES
languageA = list(language.keys())
lang1 = languageA

# Create a dropdown menu for selecting the source language
combo1 = ttk.Combobox(root, values=languageA, font="Montserrat 14", state="readonly")
combo1.place(x=100, y=20)
combo1.set("ENGLISH")  # Set the default source language to English

# Create a label displaying the current selected language in a large, bold font
label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Create a black frame with a border to contain the input text box and scrollbar
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)


# Create a Text widget for entering input text
text1 = Text(f,
            font="Montserrat 20",  # Set the font of the text
            bg="white",            # Set the background color to white
            relief=GROOVE,        # Add a grooved border
            wrap=WORD)           # Wrap text to words at line breaks

# Place the text box within the frame
text1.place(x=0, y=0, width=430, height=200)

# Create a vertical scrollbar for the text box
scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")  # Pack the scrollbar on the right side, filling the vertical space

# Connect the scrollbar to the text box for scrolling
scrollbar1.configure(command=text1.yview)  # Update scrollbar position based on text box vertical movement
text1.configure(yscrollcommand=scrollbar1.set)  # Update text box view based on scrollbar position

# Create a combobox for target language selection
combo2 = ttk.Combobox(root, values=languageA, font="Montserrat 14", state="readonly")  # Read-only to prevent manual editing
combo2.place(x=730, y=20)  # Position the combobox
combo2.set("Select Language")  # Set the initial prompt

# Create a label for the target language
label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)  # Position the label

# Create a frame for the output text box
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)  # Position the frame

# Create the output text box
text2 = Text(f1, font="Montserrat 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

# Create a scrollbar for the output text box
scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")  # Attach the scrollbar to the right side of the frame

# Link the scrollbar to the output text box
scrollbar2.configure(command=text2.yview)  # Scrollbar controls text2's vertical scrolling
text2.configure(yscrollcommand=scrollbar2.set)  # text2 updates scrollbar's position

# Create a "Translate" button
translate_button = Button(root, text="Translate", font="Montserrat 15 bold italic",
                          activebackground="red", cursor="hand1", bd=5, bg="red", fg="white",
                          command=translate_now)
translate_button.place(x=480, y=250)  # Position the button

# Call the label_change function (uncomment if needed)
# label_change()  # Not relevant in this snippet without combo boxes

# Set the background color of the window
root.configure(bg="white")

# Start the main loop of the application
root.mainloop()
