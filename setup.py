from tkinter import *
import os

def setval():
    salutaion=""
    if userGender.get() == "male":
        salutaion = "sir"
    elif userGender.get() == "female":
        salutaion = "mam"
    voice =0
    if assistGender.get() == "male":
        voice = 0
    elif assistGender.get() == "female":
        voice = 1

    fileObj = open("setup.txt","w+")
    fileObj.write(f"{userName.get()},{assistName.get()},{voice},{salutaion},{assistRate.get()}")
    fileObj.close()
    root.destroy()

root = Tk()
root.title(os.getcwd()+"\\Assistant setup")
root.geometry("400x250")

# defining labels
name = Label(root, text="Name :")
gender = Label(root, text="Gender :")
assistantName =Label(root, text="Assistant Name :")
assistantGender = Label(root, text="Assistant Voice :")
# salutation gender set according to gender
assistantRate = Label(root, text="Voice Rate :")

# setting up variable
userName = StringVar()
userGender = StringVar()
userGender.set("male")
assistName = StringVar()
assistGender = StringVar()
assistGender.set("female")
assistRate = IntVar()


# taking inputs
userNameEntry = Entry(root, textvariable = userName)
userGenderEntry = Radiobutton(root, text ="Male", variable=userGender, value = "male")
userGenderEntry1 = Radiobutton(root, text ="Female", variable=userGender, value = "female")
assistantNameEntry = Entry(root, textvariable = assistName)
assistantGenderEntry = Radiobutton(root, text ="Male", variable=assistGender, value = "male")
assistantGenderEntry1 = Radiobutton(root, text ="Female", variable=assistGender, value = "female")
assistantRateEntry = Entry(root, textvariable = assistRate)
btn =Button(root, text= "Submit", command= setval)

# packing widget
name.grid(row=0 , column=0 , ipadx=10, ipady= 3, padx=5, pady= 5)
gender.grid(row=1 , column=0 , ipadx=10, ipady= 3, padx=5, pady= 5)
assistantName.grid(row=2 , column=0, ipadx=10, ipady= 3, padx=5, pady= 5)
assistantGender.grid(row=3, column=0, ipadx=10, ipady= 3, padx=5, pady= 5)
assistantRate.grid(row=4, column=0, ipadx=10, ipady= 3, padx=5, pady= 5)
userNameEntry.grid(row=0, column=1,columnspan=2, ipadx=60, ipady= 3, padx=5, pady= 5)
userGenderEntry.grid(row=1, column=1, ipadx=10, ipady= 3, padx=5, pady= 5)
userGenderEntry1.grid(row=1, column=2, ipadx=10, ipady= 3, padx=5, pady= 5)
assistantNameEntry.grid(row=2, column=1,columnspan=2, ipadx=60, ipady= 3, padx=5, pady= 5)
assistantGenderEntry.grid(row=3, column=1, ipadx=10, ipady= 3, padx=5, pady= 5)
assistantGenderEntry1.grid(row=3, column=2, ipadx=10, ipady= 3, padx=5, pady= 5)
assistantRateEntry.grid(row=4, column=1, columnspan=2, ipadx=60, ipady= 3, padx=5, pady= 5)
btn.grid(row=5, column=1, ipadx=10, ipady= 3, padx=5, pady= 5)


root.mainloop()
