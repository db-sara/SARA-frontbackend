from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import os
from datetime import date as d

def perform():
    if sentiment_analysis.get():
            file = askopenfile()
            contents = file.read()
            file_to_analyze.insert(END, contents)
            source2.insert(END, os.path.basename(file.name))
            date2.insert(END, d.today())
            json2.insert(END, "Call sentiment analysis API and place json result here\n")
            
    if(not company.get()):
        messagebox.showerror("Error", "Enter Company Name")
    else:
        if risk_report.get():
            json.insert(END, "Call risk report API and place json result here\n")
        if financial_data.get():
            json3.insert(END, "Call web scraping API and place json result here\n")

def setup():
    global company, risk_report, financial_data, sentiment_analysis, file_to_analyze, source, num_results, date, json
    global source2, num_results2, date2, json2, source3, num_results3, date3, json3

    root = Tk()
    root.title('Text Widget Demo')
    root.geometry('850x1200')

    company_m = Message(root, width=200, font=('Courier', 14), text="Enter Company Name").place(anchor=NW, x=400, y=0)
    company = Entry(root, width=20, font=('Courier', 14))
    company.place(anchor=NW, x=400, y=30)
    Button(root, text='Perform', font=('Helvetica', 14),
        command=perform).place(anchor=NW, x=465, y=100)
    
    #Options 
    risk_report = BooleanVar()
    financial_data = BooleanVar()
    #social_data = BooleanVar()
    sentiment_analysis = BooleanVar()

    options = Frame(root, bg='lightblue')

    options_m = Message(root, width=200, font=('Courier', 14), text="Options").place(anchor=NW, x=40, y=0)
    Checkbutton(options, bg='lightblue', text='Risk Report', var=risk_report).pack(anchor=W)
    Checkbutton(options, bg='lightblue', text='Financial Data', var=financial_data).pack(anchor=W)
    Checkbutton(options, bg='lightblue', text='Sentiment Analysis', var=sentiment_analysis).pack(anchor=W)
    options.place(anchor=NW, x=40, y=31)

    file_to_analyze_m = Message(root, width=200, font=('Courier', 14), text="File to Analyze").place(anchor=NW, x=195, y=0)
    file_to_analyze = Text(root, width=18, height=10)
    file_to_analyze.place(anchor=NW, x=210, y=30)

    source_m = Message(root, width=100, font=('Courier', 14), text="Source").place(anchor=NW, x=40, y=225)
    source = Text(root, width=13, height=1, font=('Courier', 12))
    source.place(anchor=NW, x=40, y=250)
    
    num_results_m = Message(root, width=200, font=('Courier', 14), text="Num Results").place(anchor=NW, x=40, y=275)
    num_results = Text(root, width=13, height=1, font=('Courier', 12))
    num_results.place(anchor=NW, x=40, y=300)
    
    date_m = Message(root, width=100, font=('Courier', 14), text="Date").place(anchor=NW, x=40, y=325)
    date = Text(root, width=13, height=1, font=('Courier', 12))
    date.place(anchor=NW, x=40, y=350)

    json_m = Message(root, width=200, font=('Courier', 14), text="Risk Report").place(anchor=NW, x=420, y=225)
    json = Text(root, width=50, height = 10, font=('Courier', 12))
    json.place(anchor=NE, x=765, y=250)
###
    source2_m = Message(root, width=100, font=('Courier', 14), text="Source").place(anchor=NW, x=40, y=475)
    source2 = Text(root, width=13, height=1, font=('Courier', 12))
    source2.place(anchor=NW, x=40, y=500)
    
    num_results2_m = Message(root, width=200, font=('Courier', 14), text="Num Results").place(anchor=NW, x=40, y=525)
    num_results2 = Text(root, width=13, height=1, font=('Courier', 12))
    num_results2.place(anchor=NW, x=40, y=550)
    
    date2_m = Message(root, width=100, font=('Courier', 14), text="Date").place(anchor=NW, x=40, y=575)
    date2 = Text(root, width=13, height=1, font=('Courier', 12))
    date2.place(anchor=NW, x=40, y=600)

    json2_m = Message(root, width=200, font=('Courier', 14), text="Sentiment").place(anchor=NW, x=435, y=475)
    json2 = Text(root, width=50, height = 10, font=('Courier', 12))
    json2.place(anchor=NE, x=765, y=500)
###
    source3_m = Message(root, width=100, font=('Courier', 14), text="Source").place(anchor=NW, x=40, y=725)
    source3 = Text(root, width=13, height=1, font=('Courier', 12))
    source3.place(anchor=NW, x=40, y=750)
    
    num_results3_m = Message(root, width=200, font=('Courier', 14), text="Num Results").place(anchor=NW, x=40, y=775)
    num_results3 = Text(root, width=13, height=1, font=('Courier', 12))
    num_results3.place(anchor=NW, x=40, y=800)
    
    date3_m = Message(root, width=100, font=('Courier', 14), text="Date").place(anchor=NW, x=40, y=825)
    date3 = Text(root, width=13, height=1, font=('Courier', 12))
    date3.place(anchor=NW, x=40, y=850)

    json3_m = Message(root, width=200, font=('Courier', 14), text="Social/Financial").place(anchor=NW, x=400, y=725)
    json3 = Text(root, width=50, height = 10, font=('Courier', 12))
    json3.place(anchor=NE, x=765, y=750) 
    
setup()

