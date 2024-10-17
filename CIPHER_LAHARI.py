import tkinter as tk  # Importing the Tkinter library for creating GUI
from tkinter import messagebox  # Importing the messagebox module for pop-up messages
# Function to perform Caesar Cipher (both encryption and decryption)
def Cipher(text,shift,mode):
    Encrypted_text=""
    for i in text:
        #Considering text= LAhAri as my text just for explanation.
        #L is capital so changing it first into normal considering A---->0 OR a----->0
        if i.isalpha():
            shift_base= ord('A') if i.isupper() else ord('a')
            if mode == "decrypt":
                Encrypted_text+=chr(((ord(i)-shift_base-shift)%26)+shift_base)
            else:
                Encrypted_text+=chr(((ord(i)-shift_base+shift)%26)+shift_base)
            '''h=72---> h=72-65==7----> + (shift=25)=== 32---> 33%26=6--->
                    6+65=71---> ord(71)=g
                   L=108---> h=108-97=11----> + (shift=25)=== 36---> 37%26=10--->
                    10+97=107---> ord(107)=K'''
        else:
            Encrypted_text+=i  #it represents that the non alphabets are not changed
    return Encrypted_text #RESULT 
# Function to process the input text from the user
def process_text():
    text = entry_text.get()  # Get the text from the input box
    shift = entry_shift.get()  # Get the shift value from the input box
    
    try:
        shift = int(shift)  # Convert the shift value to an integer
        
        # Validate if the shift value is within the valid range (0-25)
        if shift < 0 or shift > 25:
            raise ValueError("Shift must be between 0 and 25.")  # Raise an error if out of range

        mode = selected_mode.get()  # Get whether the user selected encryption or decryption
        result = Cipher(text, shift, mode)  # Call the Caesar Cipher function
        
        # Update the result label to display the encrypted or decrypted text
        label_result.config(text=f"Result: {result}")
    except ValueError as ve:
        # If the shift value is invalid, show an error message to the user
        messagebox.showerror("Input Error", str(ve))

# Creating the main application window
window = tk.Tk()
window.title("Caesar Cipher GUI")  # Set the title of the window

# Creating and placing the label and entry field for the text input
label_text = tk.Label(window, text="Enter Text:")  # Label for the text input
label_text.pack()  # Pack (place) the label in the window

entry_text = tk.Entry(window, width=50)  # Entry box where the user types the text
entry_text.pack()  # Pack (place) the entry box in the window

# Creating and placing the label and entry field for the shift value input
label_shift = tk.Label(window, text="Enter Shift (0-25):")  # Label for the shift input
label_shift.pack()  # Pack (place) the label in the window

entry_shift = tk.Entry(window, width=5)  # Entry box for the shift value
entry_shift.pack()  # Pack (place) the entry box in the window

# Variable to store the user's choice (Encrypt or Decrypt)
selected_mode = tk.StringVar(value="encrypt")  # Default value is "encrypt"

# Creating and placing radio buttons for selecting either Encrypt or Decrypt
radio_encrypt = tk.Radiobutton(window, text="Encrypt", variable=selected_mode, value="encrypt")
radio_encrypt.pack()  # Pack (place) the Encrypt radio button in the window

radio_decrypt = tk.Radiobutton(window, text="Decrypt", variable=selected_mode, value="decrypt")
radio_decrypt.pack()  # Pack (place) the Decrypt radio button in the window

# Creating and placing the Process button that triggers the process_text function
button_process = tk.Button(window, text="Process", command=process_text)
button_process.pack()  # Pack (place) the Process button in the window

# Label for displaying the result of the encryption or decryption
label_result = tk.Label(window, text="")  # Empty label where result will be shown
label_result.pack()  # Pack (place) the label in the window

# Start the main GUI loop to keep the application running
window.mainloop()
