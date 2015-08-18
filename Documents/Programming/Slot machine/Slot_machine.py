from Tkinter import *
import time, random

window = Tk()
window.title('Slots')

frame1 = PhotoImage(file='fruit-machine-handle.gif', format="gif -index 1")
frame2 = PhotoImage(file='fruit-machine-handle.gif', format="gif -index 2")
frame3 = PhotoImage(file='fruit-machine-handle.gif', format="gif -index 3")
frame4 = PhotoImage(file='fruit-machine-handle.gif', format="gif -index 4")

frames = [frame1, frame2, frame3, frame4]

slot_gif = frame1

slotwidth = 1
slotheight = 1

slot1text = '0'

slot1 = Label(window, text = slot1text, bg = 'white', fg = 'red', width=slotwidth, height=slotheight, font=("Helvetica", 40))
slot1.pack(side = LEFT, padx = 2, pady = 3)

slot2text = '0'

slot2 = Label(window, text = slot2text, bg = 'white', fg = 'red', width=slotwidth, height=slotheight, font=("Helvetica", 40))
slot2.pack(side = LEFT, padx = 2, pady = 3)

slot3text = '0'

slot3 = Label(window, text = slot3text, bg = 'white', fg = 'red', width=slotwidth, height=slotheight, font=("Helvetica", 40))
slot3.pack(side = LEFT, padx = 2, pady = 3)

spinmoney = 1000

money = Label(window, text=spinmoney)
money.pack(side=TOP, pady = 3)

def checkifwin():
    global spinmoney, slot1text, slot2text, slot3text

    if slot1text == '7':
        if slot2text == '7':
            if slot3text == '7':
                spinmoney += 1000000

    elif slot1text == '!':
        if slot2text == '!':
            if slot3text == '!':
                spinmoney += 500000

    elif slot1text == '*':
        if slot2text == '*':
            if slot3text == '*':
                spinmoney += 100000

    elif slot1text == '?':
        if slot2text == '?':
            if slot3text == '?':
                spinmoney += random.randint(50000,100000)

    elif slot1text == '$':
        if slot2text == '$':
            if slot3text == '$':
                spinmoney += 10000

    elif slot1text == '0':
        if slot2text == '0':
            if slot3text == '0':
                spinmoney +=  100

    money.config(text = spinmoney)

def spinslots():
    global slot1text, slot2text, slot3text, spinmoney, slot_gif, frames, frame1, frame2, frame3, frame4



    if spinmoney >= 100:
        spinmoney-=100
        window.update()

        for i in range(0,4):
            slot_gif = frames[i]
            doslot.config(image=slot_gif)
            window.update()
            time.sleep(0.1)

        for i in range(3,-1,-1):
            slot_gif = frames[i]
            doslot.config(image=slot_gif)
            window.update()
            time.sleep(0.1)

        high_chance_outcomes = ['000','$$$','0$$','00$','$$0','$00','0$0','$0$']
        med_chance_outcomes = ['***','???','*??','**?','??*','?**','*?*','?*?']
        low_chance_outcomes = ['777','!!!','7!!','77!','!!7','!77','!7!','7!7']
        all_outcomes = ['000','$$$','0$$','00$','$$0','$00','0$0','$0$', '***','???','*??','**?','??*','?**','*?*','?*?', '777','!!!','7!!','77!','!!7','!77','!7!','7!7']

        for i in range(0,15):

            newslottext = all_outcomes[random.randint(0, (len(all_outcomes)-1))]
            newslottext.split()

            slot1text = newslottext[0]
            slot2text = newslottext[1]
            slot3text = newslottext[2]

            slot1.config(text = slot1text)
            slot2.config(text = slot2text)
            slot3.config(text = slot3text)

            window.update()

            time.sleep(0.1)
            
        if random.randint(0,1) == 1:
            newslottext = high_chance_outcomes[random.randint(0, (len(high_chance_outcomes)-1))]
            newslottext.split()
            slot1text = newslottext[0]
            slot2text = newslottext[1]
            slot3text = newslottext[2]

        elif random.randint(0,1) == 1:
            newslottext = med_chance_outcomes[random.randint(0, (len(med_chance_outcomes)-1))]
            newslottext.split()
            slot1text = newslottext[0]
            slot2text = newslottext[1]
            slot3text = newslottext[2]
    
        elif random.randint(0,1) == 1:
            newslottext = low_chance_outcomes[random.randint(0, (len(low_chance_outcomes)-1))]
            newslottext.split()
            slot1text = newslottext[0]
            slot2text = newslottext[1]
            slot3text = newslottext[2]
    
        slot1.config(text = slot1text)
        slot2.config(text = slot2text)
        slot3.config(text = slot3text)

        checkifwin()

    else:
        spinmoney = 'Not Enough Money'
        money.config(text = spinmoney)
        window.update()
        time.sleep(0.5)
        spinmoney = 'YOU LOSE!'
        money.config(text = spinmoney)
        window.update()
        time.sleep(0.5)
        spinmoney = 1000
        money.config(text = spinmoney)
        window.update()
        
doslot = Button(window, command = spinslots, image = slot_gif)
doslot.pack(pady = 3, side = TOP)

mainloop()
