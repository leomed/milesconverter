from tkinter import *

window = Tk()
window.title("Mile converter")
window.minsize(width=300, height=300)




input_number = Entry(width=20)
input_number.grid(column=4, row=4)

def miles_converter():
    km_number = 1.609344
    number = float(input_number.get())
    result =  number * km_number
    label_km_converted["text"] = round(result)



label_miles = Label(text="Miles")
label_miles.grid(column=7,row=4)

label_is = Label(text="equal to")
label_is.grid(column=0,row=5)

label_km_converted = Label(text="0")
label_km_converted.grid(column=4,row=5)


label_km = Label(text="Km")
label_km.grid(column=7,row=5)


calculate_button = Button(text="Calculate", command=miles_converter)
calculate_button.grid(column=4,row=6)








window.mainloop()