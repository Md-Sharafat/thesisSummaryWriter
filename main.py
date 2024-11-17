import tkinter as tk
from newspaper import Article
from textblob import TextBlob


def summarize():
    url = link.get('1.0', "end").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    date.config(state="normal")
    summary.config(state="normal")


    title.delete('1.0', "end")
    title.insert('1.0', article.title)

    author.delete('1.0', "end")
    author.insert('1.0', ', '.join(article.authors))

    date.delete('1.0', "end")
    date.insert('1.0', str(article.publish_date))

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)



    title.config(state="disabled")
    author.config(state="disabled")
    date.config(state="disabled")
    summary.config(state="disabled")



# Create the GUI
root = tk.Tk()
root.title("Paper Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=2, width=100)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=2, width=100)
author.config(state='disabled', bg='#dddddd')
author.pack()

dlabel = tk.Label(root, text="Publication Date")
dlabel.pack()

date = tk.Text(root, height=2, width=100)
date.config(state='disabled', bg='#dddddd')
date.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=100)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

ulabel = tk.Label(root, text="Paper URL")
ulabel.pack()

link = tk.Text(root, height=2, width=100)
link.config(bg='#dddddd')
link.pack()



btn = tk.Button(root, text="Summarize", command=summarize)
btn.config(bg='#8796aa')
btn.pack()

root.mainloop()
