from tkinter import *
import pyshorteners
root = Tk()
root.geometry("700x500") # window size
root.title("URL Shortener") # title

# input 
url_input = Entry(root, font=("Helvetica", 16))
url_input.grid(row=1, column=0, pady=6)

# label shrotened url
str_url = StringVar(root)
shortened_url = Entry(root, textvariable=str_url, font=("Helvetica", 16), fg="#fff", bg="medium sea green")
shortened_url.grid(row=3, column=2, pady=6)

# shorten url
def shorten():
	try:
		s = pyshorteners.Shortener()
		url = url_input.get()
		final_result = s.tinyurl.short(url)
		str_url.set(final_result)
		url_input.delete(0, END)
	except:
		str_url.set("Enter url first")

# button to shortnen
btn = Button(root, text="Shorten URL", padx=8, pady=4, bg="#2ecc71", fg="#fff", font=("Helvetica", 16), activebackground="#16a085", command=shorten)
btn.grid(row=2, column=2, pady=6)
root.mainloop()