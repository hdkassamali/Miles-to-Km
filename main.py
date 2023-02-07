from tkinter import *


def miles_to_km():
    miles_input = float(input.get())
    km_output = round(miles_input * 1.609)
    converted_km.config(text=km_output)


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

#input widget
input = Entry(width=7)
input.grid(column=1, row=0)

#Miles Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

#Is equal to label
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

#convertedKM label
converted_km = Label(text="0")
converted_km.grid(column=1, row=1)

#KM Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#calculate button
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)


window.mainloop()
