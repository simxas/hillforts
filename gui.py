import os
import webbrowser
import backend
from tkinter import *
from tkinter import messagebox

class Hilforts_GUI:
    def __init__(self, window):
        self.window = window
        window.title('Hillforts')
        window.resizable(width=False, height=False)

        self.hillforts_lbl = Label(window, text='Hillforts:')
        # splitting this in to second row because otherwise name_lbl will return None
        self.hillforts_lbl.grid(row=0, column=0)
        self.region_lbl = Label(window, text='Regions:')
        self.region_lbl.grid(row=0, column=3)
        self.search_forts_lbl = Label(window, text='Name:')
        self.search_forts_lbl.grid(row=11, column=0)
        self.search_region_lbl = Label(window, text='Region:')
        self.search_region_lbl.grid(row=11, column=3)

        self.fort_txt = StringVar()
        self.region_txt = StringVar()

        self.fort_entry = Entry(window, textvariable=self.fort_txt)
        self.fort_entry.grid(row=11, column=1)
        self.region_entry = Entry(window, textvariable=self.region_txt)
        self.region_entry.grid(row=11, column=4)

        self.hillforts_list = Listbox(window, height=10, width=35, selectbackground='yellow')
        self.hillforts_list.grid(row=1, column=0,rowspan=10, columnspan=2)
        self.hillforts_list.bind("<<ListboxSelect>>", self.on_selection)

        self.regions_list = Listbox(window, height=10, width=35, selectbackground='yellow')
        self.regions_list.grid(row=1, column=3,rowspan=10, columnspan=2)
        self.regions_list.bind("<<ListboxSelect>>", self.on_region_selection)

        self.view_all_btn = Button(window, text='View all', width=15, command=self.view_all, bg='white')
        self.view_all_btn.grid(row=0, column=2)
        self.search_fort_btn = Button(window, text='Search by name', command=self.search_by_name, bg='white')
        self.search_fort_btn.grid(row=11, column=2)
        self.search_region_btn = Button(window, text='Search by region', command=self.search_by_region, bg='white')
        self.search_region_btn.grid(row=11, column=5)

        self.generate_by_selection_btn = Button(window, text='Generate hillfort', width=15, command=self.generate_by_selection, bg='white')
        self.generate_by_selection_btn.grid(row=12, column=0)
        self.generate_by_region_btn = Button(window, text='Generate by region', width=15, command=self.generate_by_region, bg='white')
        self.generate_by_region_btn.grid(row=12, column=3)

    def view_all(self):
        self.hillforts_list.delete(0, END)
        self.regions_list.delete(0, END)
        for row in backend.view_all_forts():
            self.hillforts_list.insert(END, row)
        for row in backend.view_all_regions():
            self.regions_list.insert(END, row)

    def search_by_name(self):
        if self.fort_txt.get() in self.hillforts_list.get(0, 'end'):
            self.hillforts_list.delete(0, END)
            self.hillforts_list.insert(END, self.fort_txt.get())

    def search_by_region(self):
        if self.region_txt.get() in self.regions_list.get(0, 'end'):
            self.regions_list.delete(0, END)
            self.regions_list.insert(END, self.region_txt.get())

    def on_selection(self, event):
        # self.selected_hillfort
        widget = event.widget
        selection=widget.curselection()
        self.selected_hillfort = widget.get(selection[0])
        print('selection:', selection, ': {0}'.format(self.selected_hillfort))

    def on_region_selection(self, event):
        # self.selected_region
        widget = event.widget
        selection=widget.curselection()
        self.selected_region = widget.get(selection[0])
        print('selection:', selection, ': {0}'.format(self.selected_region))

    def generate_by_selection(self):
        print('Starting backend with value: {0}'.format(self.selected_hillfort))
        backend.generate_by_selection(self.selected_hillfort)
        result = messagebox.askyesno('Message','Html file was saved. Do you want to open it?')
        if result == True:
            path = os.path.abspath('htmls/{0}.html'.format(self.selected_hillfort))
            url = 'file://{0}'.format(path)
            webbrowser.open(url)
        else:
            print('selected "No"')

    def generate_by_region(self):
        print('Starting backend with value: {0}'.format(self.selected_region))
        backend.generate_by_region(self.selected_region)
        result = messagebox.askyesno('Message','Html file was saved. Do you want to open it?')
        if result == True:
            path = os.path.abspath('htmls/{0}.html'.format(self.selected_region))
            url = 'file://{0}'.format(path)
            webbrowser.open(url)
        else:
            print('selected "No"')


window = Tk()
my_gui = Hilforts_GUI(window)
window.mainloop()
