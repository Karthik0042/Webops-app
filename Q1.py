from tkinter import *

# Define a function to show the About Me section
def show_about_me():
    about_me_window = Toplevel(root)
    about_me_window.title("About Me")
    about_me_window.geometry("400x300")
    about_me_label = Label(about_me_window, text="Hi, I'm R Karthik. I'm a python based developer in chennai.\n"
                                                 "I have experience in front-end app development using flutter.\n"
                                                 "I was part of the wining team in buildathon \n "
                                                 "last sem working under Shubhan \n"
                                                 "I really dont have experience of working with HTML but joining \n"
                                                 "the team would allow me to learn the basics of web development \n "
                                                 "and work in projects that are fascinating \n "
                                                 "My Hobbies include Dancing,Pencil Sketching and listening to music"
                                                 )

    about_me_label.pack(padx=10, pady=10)

# Define a function to show the Contact Me section
def show_contact_me():
    contact_me_window = Toplevel(root)
    contact_me_window.title("Contact Me")
    contact_me_window.geometry("400x300")
    contact_me_label = Label(contact_me_window, text="You can contact me at bs22b022@smail.iitm.ac.in \n"
                                                     "or via phone at 7090675298.")
    contact_me_label.pack(padx=10, pady=10)

# Define a function to show the Projects section
def show_projects():
    projects_window = Toplevel(root)
    projects_window.title("Projects")
    projects_window.geometry("400x300")
    projects_label = Label(projects_window, text="Here's a list of my recent projects:\n"
                                                 "1. https://github.com/Karthik0042/Photo-Translate\n"
                                                 "This is the only major project i was part of last sem"
                                                    )
    projects_label.pack(padx=10, pady=10)

# Create the main window
root = Tk()
root.title("My Portfolio")

# Set window size and position
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Set window icon


# Set window background color
root.configure(background="#f2f2f2")

# Create a label for the header
header_label = Label(root, text="Welcome to my Portfolio", font=("Arial", 20, "bold"), pady=20)
header_label.pack()

# Create a button to show the About Me section
about_me_button = Button(root, text="About Me", font=("Arial", 14), command=show_about_me)
about_me_button.pack(pady=10)

# Create a button to show the Contact Me section
contact_me_button = Button(root, text="Contact Me", font=("Arial", 14), command=show_contact_me)
contact_me_button.pack(pady=10)

# Create a button to show the Projects section
projects_button = Button(root, text="Projects", font=("Arial", 14), command=show_projects)
projects_button.pack(pady=10)

# Run the main loop
root.mainloop()
