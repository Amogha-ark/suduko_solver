#Suduko solver using tk

#Suduko Question in matrix form !!
mat=[[1,0,0,4,8,9,0,0,6],
    [7,3,0,0,0,0,0,4,0],
    [0,0,0,0,0,1,2,9,5],
    [0,0,7,1,2,0,6,0,0],
    [5,0,0,7,0,3,0,0,8],
    [0,0,6,0,9,5,7,0,0],
    [9,1,4,6,0,0,0,0,0],
    [0,2,0,0,0,0,0,3,7],
    [8,0,0,5,1,2,0,0,4]]

# mat=[
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

import tkinter as tk

root = tk.Tk()
root.title("Suduko solver !!")
# specify size of window.
root.geometry("400x500")

# Create label
l = tk.Label(root, text="""Suduko Solver !! """)
l.config(font=("Courier", 14))
l.grid(row=0,column=0,columnspan=9,pady=10)

#Display section !!
def create_display():
    dd=[]
    linex = 0
    liney=0
    for i in range(1,10):
        gap = 30
        if i == 4 or i == 7:
            linex = 5
        else:
            linex = 0
        for j in range(9):

            T = tk.Text(root, height=2, width=4)
            if mat[i-1][j] == 0:
                pass
            else:
                T.config(state='normal')
                T.insert(tk.END,str(mat[i-1][j]))
                T.config(state='disabled')
            if j==2 or j==5:
                liney=5
            T.grid(row=i,column=j,padx=(gap,liney),pady=(linex,0))
            gap=0
            liney=0


            dd.append(T)
    return dd

dd = create_display()
        # print(T.get("1.0","end"),end=' ')
# print(dd[0].get("1.0","end"))

def check_finished(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j]==0:
                return False
    return True

def copy_arr(arr):
    sa1=[]
    for i in range(9):
        sa1.append([0]*9)
    for i in range(0,9):
        for j in range(9):
            sa1[i][j] = arr[i][j]
    return sa1

def is_valid(x,y,num,ma):

    #To check row
    for i in range(9):
        if ma[i][y]==num:
            return False
    #To check col
    for j in range(9):
        if ma[x][j]==num:
            return False
    p1=x//3
    p2=y//3
    #To check box
    for i in range(p1*3,(p1*3)+3):
        for j in range(p2*3,(p2*3)+3):
            if ma[i][j]==num:
                return False
    return True


def find_empty(ma):
    for i in range(9):
        for j in range(9):
            if ma[i][j]==0:
                return i,j
    return -1


def solve(ma):

    if find_empty(ma) ==-1:
        return True

    x,y=find_empty(ma)

    for i in range(1,10):
        if is_valid(x,y,i,ma):

            ma[x][y]=i

            if solve(ma):
                return True
            ma[x][y]=0
    return False


#ADD Button to add number into the box !!

def mybuton():
    bo = []
    for i in range(9):
        bo.append([0]*9)
    k=0
    for i in range(9):
        for j in range(9):
            l = dd[k].get("1.0","end")
            # print(k,l[0])
            if l[0]  == """\n""":
                bo[i][j] = 0
            else:
                # print(l[0])
                bo[i][j] = int(l[0])
            k+=1
    check=copy_arr(bo)
    dump = bo
    outptxt = tk.Text(root,width=25,height = 2)
    answer=''
    # print(dump)
    if solve(dump):
        print(dump)
        # print(check)
        answer='correct num you added !! '
        outptxt.insert(tk.END,answer)
        if check_finished(check):
            outptxt.delete("1.0","end")
            outptxt.insert(tk.END,'Hooray Finished !!')
    else:
        answer="wrong number you added !!"
        outptxt.insert(tk.END, answer)
    outptxt.grid(row=14,column=1,columnspan=8,pady=10)


def clr_button():
    # print(len(bo),len(bo[0]))
    k = 0
    for i in range(9):
        for j in range(9):
            l = dd[k].get("1.0", "end")
            if l:
                dd[k].delete("1.0", "end")
            # print(k,l[0])
            # if l[0]  == """\n""":
            if mat[i][j]!=0:
                dd[k].insert("1.0", mat[i][j])
            k+=1


def finalsol():
    ans = mat
    solve(ans)
    k=0
    for i in range(9):
        for j in range(9):
            l = dd[k].get("1.0","end")
            if l:
                dd[k].delete("1.0","end")
            # print(k,l[0])
            # if l[0]  == """\n""":
            dd[k].insert("1.0",ans[i][j])
            # else:
            #     pass
                # print(l[0])
                # bo[i][j] = int(l[0])
            k+=1
    k=0



myb = tk.Button(root,text="ADD",command=mybuton)
myb.grid(row=11,column=0,columnspan=3,pady=10)

clr = tk.Button(root,text="Clear",command=clr_button)
clr.grid(row=11,column=3,columnspan=3,pady=10)

fin = tk.Button(root,text="Give up !!",command=finalsol)
fin.grid(row=11,column=6,columnspan=3,pady=10)
# Insert The Fact.

tk.mainloop()