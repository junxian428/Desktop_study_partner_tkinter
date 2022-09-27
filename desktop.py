from re import X
import tkinter as tk # Python 3
#
import time
root = tk.Tk()
# The image must be stored to Tk or it will be garbage collected.
#sys.setrecursionlimit(10000)

def move(event):
    x, y = root.winfo_pointerxy()
    root.geometry(f"+{x}+{y}")

#frame2 = PhotoImage(file=imagefilename, format="gif -index 2")
root.image = tk.PhotoImage(file='pic2/ezgif-frame-00'+ str(1)+'.png')

def set_image(y):
    if (y>=10 and y< 100):
        root.image = tk.PhotoImage(file='pic2/ezgif-frame-0'+ str(y)+'.png')
        root.image = root.image.zoom(6) #with 250, I ended up running out of memory
        root.image =  root.image.subsample(32) 
        label = tk.Label(root, image=root.image, bg='white', width=150, height=150)
        root.overrideredirect(True)
        root.geometry("+500+200")
        root.lift()
        root.bind('<B1-Motion>',move)
      


    elif(y>=100):
        root.image = tk.PhotoImage(file='pic2/ezgif-frame-'+ str(y)+'.png')
        root.image = root.image.zoom(6) #with 250, I ended up running out of memory
        root.image =  root.image.subsample(32) 
        label = tk.Label(root, image=root.image, bg='white', width=150, height=150)
        root.overrideredirect(True)
        root.geometry("+500+200")
        root.lift()
        root.bind('<B1-Motion>',move)
     


    else:
        root.image = tk.PhotoImage(file='pic2/ezgif-frame-00'+ str(y)+'.png')
        root.image = root.image.zoom(6) #with 250, I ended up running out of memory
        root.image =  root.image.subsample(32) 
        label = tk.Label(root, image=root.image, bg='white', width=150, height=150)
        root.overrideredirect(True)
        root.geometry("+500+200")
        root.lift()
        root.bind('<B1-Motion>',move)

  


root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "white")



root.image = root.image.zoom(6) #with 250, I ended up running out of memory
root.image =  root.image.subsample(32) #mechanically, here it is adjusted to 32 instead of 320



    #root.image = tk.PhotoImage(file='ezgif-frame-001.png')

   

#frameCnt = 12

#root.image = [tk.PhotoImage(file='image.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
#frames = [PhotoImage(file='mygif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

#root.image = tk.PhotoImage(file="image.gif")
#rint()
#def update(ind):

    #frame = root.image[ind]
    #ind += 1
    #if ind == frameCnt:
        #ind = 0
    #label.configure(image=frame)
    #root.after(100, update, ind)





#resized_image= img.resize((300,205), Image.ANTIALIAS)
root.image = tk.PhotoImage(file='pic2/ezgif-frame-00'+ str(1)+'.png')
root.image = root.image.zoom(6) #with 250, I ended up running out of memory
root.image =  root.image.subsample(32) 

label = tk.Label(root, image=root.image, bg='white', width=150, height=150)
#root.configure(image=root.image,bg='white', width=150, height=150)

root.overrideredirect(True)
root.geometry("+500+200")
root.lift()
root.bind('<B1-Motion>',move)


root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "white")
#root.after(100, updateFrame(1))

label.pack()
x= 1
def callback(event=None):
    global x

    print("Running................" + str(x))
    if(x>=151):
        x = 1
        img2 = tk.PhotoImage(file='pic2/ezgif-frame-00'+ str(x)+'.png')
    elif(x==55):
        x = 78
        img2 = tk.PhotoImage(file='pic2/ezgif-frame-0'+ str(x)+'.png')
    elif(x<= 150 and x >=100):
        img2 = tk.PhotoImage(file='pic2/ezgif-frame-'+ str(x)+'.png')
    elif (x>=10 and x<= 99):
        img2 = tk.PhotoImage(file='pic2/ezgif-frame-0'+ str(x)+'.png')
    elif(x<10):
        img2 = tk.PhotoImage(file='pic2/ezgif-frame-00'+ str(x)+'.png')
    else:
        print("Error!!!!!!!!")

    img2 = img2.zoom(6)
    img2 = img2.subsample(32) 

    label.configure(image=img2, bg='white', width=150, height=150)
    root.image = img2
    x = x + 1
    root.after(100,callback)


root.after(100,callback)

#root.bind("<Enter>", callback)



label.mainloop()

