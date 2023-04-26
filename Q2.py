from tkinter import *
from tkinter import ttk
import webbrowser
import requests
from bs4 import BeautifulSoup

chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
def on_entry_click(event):
    """Function that gets called whenever the search entry is clicked"""
    if search_entry.get() == 'Enter search query...':
        search_entry.delete(0, "end")  # delete all the text in the entry
        search_entry.insert(0, '')  # Insert blank for user input
        search_entry.config(fg='black')

def on_focusout(event):
    """Function that gets called whenever the search entry loses focus"""
    if search_entry.get() == '':
        search_entry.insert(0, 'Enter search query...')
        search_entry.config(fg='grey')

def on_key_press(event):
    """Function that gets called whenever a key is pressed in the search entry"""
    if event.keycode == 13:  # Enter key pressed
        search()

def search():
    """Function that gets called when the search button is clicked"""
    query = search_entry.get()
    url = 'https://www.google.com/search?q=' + query
    search_results = requests.get(url)
    soup = BeautifulSoup(search_results.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href.startswith('/url?q='):
            url = href.replace('/url?q=', '').split('&')[0]
            webbrowser.get(chrome_path).open_new(url)
            break

root = Tk()
root.title("Search Engine")

# Set up window size and position
window_width = 600
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Set up window background color
root.configure(background="#f2f2f2")

# Create a label and entry widget for the search query
search_entry = ttk.Entry(root, width=50, font=("Helvetica", 12), foreground='grey')
search_entry.insert(0, 'Enter search query...')
search_entry.bind('<FocusIn>', on_entry_click)
search_entry.bind('<FocusOut>', on_focusout)
search_entry.bind('<Key>', on_key_press)
search_entry.grid(row=0, column=0, padx=10, pady=10)

# Create a button to start the search
search_button = ttk.Button(root, text="Search", command=search, style='Google.TButton')
search_button.grid(row=0, column=1, padx=10, pady=10)

# Define the Google-themed style for the button
style = ttk.Style()
style.theme_create('Google', parent='alt', settings={
    'TButton': {
        'configure': {
            'background': '#4285F4',
            'foreground': 'white',
            'font': ('Helvetica', 12),
            'padding': 5,
            'borderwidth': 0,
            'width': 10
        },
        'map': {
            'background': [('hover', '#3278b5'),
                           ('active', '#1177d9'),
                           ]
        }
    }
})

style.theme_use('Google')

root.bind('<KeyPress-/>', lambda event: root.destroy())

root.mainloop()
