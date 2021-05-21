import sys
import os
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
#from syntaxtheme import *
syn = open("syntaxtheme.py", "r")
syntaxtheme_code = syn.read()
syn.close()
suggestionsList = []
fileExtensions = ".txt"
fontsize = 15

onButtonChange = None
onEnding = None

syntaxtheme = compile(syntaxtheme_code, "syntaxtheme.py", 'exec')
exec(syntaxtheme)
#suggestionsList = syntaxtheme.suggestionsList

#print(suggestionsList)
suggestionsList.sort (key=len)

def matchingInPercent (word:str, base:str):
    if len(word) > len(base):
        return 0.0
    
    points = 0
    for i in range (len(word)):
        #print (base, " -> " + word[i] + " == " + base[i] + " => " + str(word[i] == base[i]))
        if word[i] == base[i]:
            points += 1
        else:
            return 0.0
    #print (base + " -> Points: " + points)
    if not (len(base) > 0):
        return 0.0
    if (float(points) / float(len(base))) >= 1.0:
        return 0.0
    return float(points) / float(len(base))


def suggest (suggestions, word):
    for x in suggestions:
        if matchingInPercent (word, x) >= 0.001:
            return x
    return ""

def checkLineLength(event):
    global editor
    global linenum
    global scrollvalue
    lenghtOfLines = int(editor.index('end').split('.')[0]) - 1
    linenum.config(state=NORMAL)
    linenum.delete("1.0", END)
    for i in range(1, lenghtOfLines+1):
        linenum.insert(END, str(i))
        if i != lenghtOfLines:
            linenum.insert(END, "\n")
    linenum.yview("moveto", scrollvalue)
    linenum.config(state=DISABLED)
scrollvalue = ""
def setScrollT(*args):
    global linenum
    global scroll
    global scrollvalue
    linenum.yview("moveto", args[0])
    scroll.set(*args)
    scrollvalue = args[0]
def setScrollB(*args):
    global linenum
    global editor
    global scrollvalue
    linenum.yview(*args)
    editor.yview(*args)
    scrollvalue = args[0]

def clearAll():
    global window
    global linenum
    global editor
    global path
    window.title("UNNAMED SCRIPT")
    linenum.config(state=NORMAL)
    linenum.delete("1.0", END)
    linenum.insert(END, "1")
    linenum.config(state=DISABLED)
    editor.delete("1.0", END)
    path = ""
def readFile():
    global window
    global linenum
    global editor
    global abspath
    global path
    global hight
    path = askopenfilename()
    abspath = os.path.abspath(path)
    path = os.path.basename(abspath)
    window.title(path + " - " + abspath)
    file = open(abspath, "r")
    lines = file.readlines()
    lcount = 0
    linenum.config(state=NORMAL)
    linenum.delete("1.0", END)
    editor.delete("1.0",END)
    for line in lines:
        lcount += 1
        editor.insert(END, line)
        linenum.insert(END, str(lcount) + "\n")
    linenum.config(state=DISABLED)
    hightall()
def saveFile():
    global editor
    global path
    global abspath
    global window
    global fileExtensions
    if path == "":
        file = asksaveasfile(mode="w", defaultextension=fileExtensions)
        path = file.name
        abspath = os.path.abspath(path)
        path = os.path.basename(abspath)
        filetext = editor.get("1.0", END)
        file.write(filetext)
        file.close()
        window.title(path + " - " + abspath)
    else:
        file = open(abspath, "w")
        filetext = editor.get("1.0", END)
        file.write(filetext)
        file.close()
def saveAsFile():
    global path
    global abspath
    path = ""
    abspath = ""
    saveFile()
def byctrls(e):
    saveFile()
def iungodebug():
    global interpreterpath
    global abspath
    saveFile()
    #print("start cmd /k \"" + interpreterpath + "\\Iun.exe '" + abspath + "' & echo ------------------------------ & echo Exit-code: %errorlevel% & pause & exit \"")
    try:
        os.system("start cmd /k \"" + interpreterpath + "\\"+interpreterfile+" \"" + abspath + "\" & echo ------------------------------ & echo Exit-code: %errorlevel% & pause & exit \"")
    except:
        pass
changefontwindow = None
fontlist = None
def changeFontStyle():
    global fontlist
    global fontsize
    global commonfont
    global changefontwindow
    global window

    global editor
    global linenum

    if fontlist == None and fontsize == None:
        return
    commonfont = Font(family=fontlist.get(), size=fontsize.get())
    editor.config(font = commonfont)
    linenum.config(font = commonfont)
    changefontwindow.destroy()
    changefontwindow = None
    window.focus()
    updateHigh()
    hightall()
def changefontwindow_close():
    global changefontwindow
    changefontwindow.destroy()
    changefontwindow = None
def changeFont():
    global commonfont
    global window
    global changefontwindow
    global fontlist
    global fontsize
    if changefontwindow == None:
        changefontwindow = Toplevel(window)
        changefontwindow.title("Font settings")

        fontlist = ttk.Combobox(changefontwindow)
        
        fonts = list(font.families())
        fonts.sort()
        fontlist.config(values=fonts, font=commonfont)
        fontlist.focus_set()
        fontlist.set(commonfont.cget("family"))
        fontlistlabel = Label(changefontwindow, text="Font: ", font=commonfont)
        fontlistlabel.grid(row=0, column=0)

        fontsize = ttk.Combobox(changefontwindow, font=commonfont)
        fontsize.set(commonfont.cget("size"))
        chooselist = []
        for x in range(8, 73, 2):
            chooselist.append(x)
        fontsize.config(values=chooselist)

        fontsizelabel = Label(changefontwindow, text="Size: ", font=commonfont)

        fontlist.grid(row=0, column=1)
        fontsizelabel.grid(row=1, column=0)
        fontsize.grid(row=1, column=1)

        confirm = Button(changefontwindow, text="confirm", font=commonfont, command=changeFontStyle)
        confirm.grid(row=2,column=1)

        changefontwindow.protocol("WM_DELETE_WINDOW", changefontwindow_close)
    else:
        changefontwindow.focus()
def incfont(event):
    global commonfont
    global editor
    global linenum
    commonfont = Font(family=commonfont.cget("family"), size=commonfont.cget("size")+2)
    editor.config(font=commonfont)
    linenum.config(font=commonfont)
    updateHigh()
    hightall()
def decfont(event):
    global commonfont
    global editor
    global linenum
    commonfont = Font(family=commonfont.cget("family"), size=commonfont.cget("size")-2)
    editor.config(font=commonfont)
    linenum.config(font=commonfont)
    updateHigh()
    hightall()
window = Tk()
window.title("UNNAMED SCRIPT")

menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New File", command=clearAll)
filemenu.add_command(label="Open", command=readFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save as", command=saveAsFile)

blueprints_menu = Menu (window)

def setTextOfEditor (text:str):
    global editor
    editor.delete ("0.0", END)
    editor.insert ("0.0", text)
    hightall()

for x in bluePrints:
    blueprints_menu.add_command(label=x[0], command=lambda t=x[1]: setTextOfEditor(t))

filemenu.add_cascade(label="Blueprints", menu=blueprints_menu);

debugmenu = Menu(menu)
visible_menu = True

def toggelBar(event):
    global menu
    global window
    global visible_menu 
    global scroll
    if visible_menu:
        window.config(menu=Menu(window))
        visible_menu = False
        scroll.pack_forget()
    else:
        window.config(menu=menu)
        visible_menu = True
        scroll.pack(side=RIGHT, fill=Y)
visible_linenum = True
def toggelLineNumbers(event):
    global visible_linenum
    global linenum
    global editor
    if visible_linenum:
        visible_linenum = False
        linenum.pack_forget()
    else:
        visible_linenum = True
        editor.pack_forget()
        linenum.pack(side=LEFT, anchor=NW, expand=False, fill=Y)
        editor.pack(side=LEFT, anchor=NW, expand=True, fill=BOTH)
transperence = False
def toggle_transperence():
    global window
    global editor
    global linenum
    global transperence
    global transperence_level
    if transperence:
        transperence=False
        window.wm_attributes('-alpha',1.0)
    else:
        transperence=True
        window.wm_attributes('-alpha', transperence_level)
def open_config():
    os.system("start "+config_editor+" syntaxtheme.py")
menu.add_cascade(label="debug", menu=debugmenu)

debugmenu.add_command(label="Start debug",command=iungodebug)

menu.add_command(label="Start", command=iungodebug)

stylemenu = Menu(menu)
menu.add_cascade(label="Style", menu=stylemenu)

stylemenu.add_command(label="Font", command=changeFont)
stylemenu.add_command(label="Toggle transperence", command=toggle_transperence)
stylemenu.add_command(label="Open config", command=open_config)

commonfont = Font(family=familyset, size=fontsize)

scroll = Scrollbar(window)
scroll.pack(side=RIGHT, fill=Y)
linenum = Text(window, font=commonfont, width=3,state=DISABLED)
linenum.pack(side=LEFT, anchor=NW, expand=False, fill=Y)
editor = Text(window, wrap=NONE, yscrollcommand=setScrollT, font=commonfont)
editor.pack(side=LEFT, anchor=NW, expand=True, fill=BOTH)
editor.focus_set()
scroll.config(command=setScrollB)
autocomplete = Listbox(window)
autocomplete.insert(0, "cline")
def autocompletetask(event):
    global autocomplete
    global editor
    choosen = autocomplete.get(autocomplete.curselection())
    autocomplete.place_forget()
    editor.insert(END, choosen)
    editor.focus()
def closeauto(event):
    global autocomplete
    global editor
    autocomplete.place_forget()
    editor.focus()
autocomplete.bind("<Return>", autocompletetask)
autocomplete.bind("<Escape>", closeauto)
path = ""
abspath = ""
lines = []
if len (sys.argv) > 1:
    path = sys.argv[1]
    abspath = os.path.abspath(path)
    window.title(path + " - " + abspath)
    file = open(abspath, "r")
    lines = file.readlines()
    lcount = 0
    linenum.config(state=NORMAL)
    linenum.delete("1.0", END)
    for line in lines:
        lcount += 1
        editor.insert(END, line)
        linenum.insert(END, str(lcount) + "\n")
    linenum.config(state=DISABLED)
    hightall()
else:
    editor.insert(END, "")
    linenum.config(state=NORMAL)
    linenum.insert(END, str(1) + "\n")
    linenum.config(state=DISABLED)
def updateHigh():
    for x in highlight:
        if x[4] != "" and x[5] != "":
            if x[2] != backgroundcolor:
                editor.tag_configure(x[0], foreground=x[1], background=x[2], font=(commonfont.cget("family"), commonfont.cget("size"), x[4], x[5]))
            else:
                editor.tag_configure(x[0], foreground=x[1], font=(commonfont.cget("family"), commonfont.cget("size"), x[4], x[5]))
        else:
            if x[2] != backgroundcolor:
                editor.tag_configure(x[0], foreground=x[1], background=x[2], font=(commonfont.cget("family"), commonfont.cget("size"), x[4]))
            else:
                editor.tag_configure(x[0], foreground=x[1], font=(commonfont.cget("family"), commonfont.cget("size"), x[4]))
updateHigh()
def hightall():
    global editor
    global highlight
    global autocomplete
    for x in highlight:
        start = "1.0"
        end = "end"
        editor.tag_remove(x[0], start, end)
        while start != end:
            try:
                    countVar = StringVar()
                    pos = editor.search(x[0], start, stopindex=end, count=countVar, regexp=x[3])
                    if pos != "":
                        start = pos + " + " + countVar.get() + "c"
                    editor.tag_add(x[0], pos, pos + " + " + countVar.get() + "c")
            except:
                    break
def hight(event=None):
    global editor
    global highlight
    global autocomplete
    for x in highlight:
        start = editor.index(INSERT).split(".")[0] + ".0"
        end = editor.index(INSERT)
        editor.tag_remove(x[0], start, end)
        while start != end:
            try:
                    countVar = StringVar()
                    pos = editor.search(x[0], start, stopindex=end, count=countVar, regexp=x[3])
                    if pos != "":
                        start = pos + " + " + countVar.get() + "c"
                    editor.tag_add(x[0], pos, pos + " + " + countVar.get() + "c")
            except:
                    break
    checkLineLength(event)
    #pos = editor.index(INSERT);
    #print(pos)
    #autocomplete.place(x = 30, y = 30)
    #autocomplete.select_set(0)
    #autocomplete.focus()
hasWindowBar = True
def noWindowBorder(event):
    global window
    global hasWindowBar
    if hasWindowBar:
        hasWindowBar = False
        window.overrideredirect(1)
    else:
        hasWindowBar = True
        window.overrideredirect(0)

suggestion_pos = ("", "")

def deleteSuggestion (event:Event):
    global suggestion_pos
    global editor
    if event.char == " ":
        cursorpos = editor.index(INSERT)
        editor.delete (suggestion_pos[0] + "+1c", suggestion_pos[1])
        suggestion_pos = ("", "")
        editor.mark_set("insert", "%d.%d" % (int(cursorpos.split(".")[0]), int(cursorpos.split(".")[1])))

def getWordAtCharacter(text:str, pos:int):
    if not len(text) > 0:
        return ""
    while True:
        if pos < 0:
            pos += 1
            break
        if text[pos] in ".@":
            break
        if not text[pos].isalpha ():
            pos += 1
            break
        pos -= 1
    word = ""
    while True:
        if pos >= len(text):
            break
        if not text[pos].isalpha () and not text[pos] in ".@" :
            break
        word = word + text[pos]
        pos += 1
    return word

def onButtonPress (event:Event):
    global editor
    global suggestionsList
    global suggestion_pos
    global onButtonChange
    global abspath
    if onButtonChange != None:
        onButtonChange (abspath)
    cursorpos = editor.index(INSERT)

    if event.char == "\t" and suggestion_pos[0] != "" and suggestion_pos[1] != "":
        editor.tag_delete ("suggestions")
        editor.mark_set("insert", suggestion_pos[1] + "+1c")
        suggestion_pos = ("", "")
        return "break"

    if event.char == " ":
        if suggestion_pos[0] != "" and suggestion_pos[1] != "":
            editor.tag_delete ("suggestions")
            editor.delete (suggestion_pos[0] + "+1c", suggestion_pos[1] + "+1c")
            suggestion_pos = ("", "")
            editor.mark_set("insert", "%d.%d" % (int(cursorpos.split(".")[0]), int(cursorpos.split(".")[1])))
    elif event.char.isalpha () or event.char in [".", "@"]:
        if suggestion_pos[0] != "" and suggestion_pos[1] != "":
            editor.tag_delete ("suggestions")
            editor.delete (suggestion_pos[0] + "+1c", suggestion_pos[1] + "+1c")
            suggestion_pos = ("", "")
            editor.mark_set("insert", "%d.%d" % (int(cursorpos.split(".")[0]), int(cursorpos.split(".")[1])))
        word = getWordAtCharacter(
            event.widget.get(cursorpos.split(".")[0] + "." + "0", INSERT) + event.char + event.widget.get(INSERT, "end-1c linestart"), 
            int(cursorpos.split(".")[1])
        )
        # print ("|" + word + "|")
        suggestion = suggest (suggestionsList, word)
        if suggestion != "":
            editor.insert ("insert", suggestion[(len(word)) : len(suggestion)])
            editor.mark_set("insert", "%d.%d" % (int(cursorpos.split(".")[0]), int(cursorpos.split(".")[1])))
            editor.tag_add("suggestions", 
                "%d.%d" % (int(cursorpos.split(".")[0]), int(cursorpos.split(".")[1])), 
                "%d.%d" % (int(cursorpos.split(".")[0]), int(cursorpos.split(".")[1]) + (len(suggestion) - (len(word))))
            )
            suggestion_pos = (
                "%d.%d" % (int(cursorpos.split(".")[0]), int(cursorpos.split(".")[1])), 
                "%d.%d" % (int(cursorpos.split(".")[0]), int(cursorpos.split(".")[1]) + (len(suggestion) - (len(word))))
            )
            editor.tag_config("suggestions", foreground="gray")
        editor.insert ("insert", event.char)
        return "break"
    elif event.keysym == "BackSpace":
        if suggestion_pos[0] != "" and suggestion_pos[1] != "":
            editor.tag_delete ("suggestions")
            editor.delete (suggestion_pos[0], suggestion_pos[1] + "+1c")
            suggestion_pos = ("", "")
            editor.mark_set("insert", "%d.%d" % (int(cursorpos.split(".")[0]), int(cursorpos.split(".")[1])-1))
            return "break"
    else:
        if suggestion_pos[0] != "" and suggestion_pos[1] != "":
            editor.tag_delete ("suggestions")
            editor.delete (suggestion_pos[0] + "+1c", suggestion_pos[1] + "+1c")
            suggestion_pos = ("", "")
            editor.mark_set("insert", "%d.%d" % (int(cursorpos.split(".")[0]), int(cursorpos.split(".")[1])))


editor.config(bg=backgroundcolor, fg=forgroundcolor, insertbackground=forgroundcolor)
linenum.config(bg=backgroundcolor, fg=forgroundcolor)

editor.bind("<Key>", checkLineLength)
editor.bind("<Control-s>", byctrls)
editor.bind("<KeyPress>", onButtonPress)
editor.bind("<KeyRelease>", hight)
editor.bind("<Control-+>", incfont)
editor.bind("<Control-minus>", decfont)
window.bind("<F11>",
    lambda event: window.attributes("-fullscreen",
    not window.attributes("-fullscreen")))
window.bind("<F6>", toggelBar)
window.bind("<F7>", toggelLineNumbers)
window.bind("<F8>", noWindowBorder)
editor.bind ("<Button>", deleteSuggestion)
window.iconbitmap("iconIdeun.ico")
window.mainloop()
if onEnding != None:
    onEnding ()
exit (0)