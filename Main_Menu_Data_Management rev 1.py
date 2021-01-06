from tkinter import*
import tkinter as tk
from tkinter import ttk
import datetime
import time

root=tk.Tk()
root.geometry("1366x768")
root.title("PT.Cobet Cell \t Design software by Singgih Febriana   Version 1.0.")
root.configure(bg='#0a3d62')

nomer_urut_TreeView=None
def command_inputan():
    global nomer_urut_TreeView
    nomer_urut_TreeView.set(nomer_urut_TreeView.get()+1)
    nomer_urut=nomer_urut_TreeView.get()
    my_tree.insert(parent='',index='end',iid=nomer_urut,text="",values=(nomer_urut,time.strftime("%H:%M:%S"),now.strftime("%d-")+bulan[int(now.strftime("%m"))]+now.strftime("-%Y"),entry_transfer.get("1.0","end"),entry_nominal.get("1.0","end"),entry_nominal.get("1.0","end"),entry_biaya_admin.get("1.0","end"),entry_komisi.get("1.0","end")))
    print("SOFTWARE LISENSI SINGGIH FEBRIANA CORPORATION!!!!\n.\n.\nDILARANG KERAS UNTUK DIJUAL BELI")
    print("HAK PATEN SINGGIH FEBRIANA")
    print("FILE SANGAT RAHASIA!!!!")

def hapus_semua():
    entry_biaya_admin.delete(1.0,END)
    entry_komisi.delete(1.0,END)
    entry_transfer.delete(1.0,END)
    entry_nominal.delete(1.0,END)
    print("SOFTWARE LISENSI SINGGIH FEBRIANA CORPORATION!!!!\n.\n.\nDILARANG KERAS UNTUK MENGHAPUS,MENGEDIT,ATAU MENAMBAHKAN DI CODE INI!!!!")
    print("DILARANG MENGCOPYKAN FILE INI KE ORANG LAIN!!!!")


def our_command():
   pass
def select(event):
    pass
def combo_pilihan_transfer(event):
    entry_transfer.insert(0.0,str(pilihan_transfer.get()))
def combo_komisi_transfer(event):
    entry_komisi.insert(0.0,"RP." +komisi_transfer.get())
def combo_komisi_admin(event):
    entry_biaya_admin.insert(0.0,"Rp." +komisi_admin.get())
#data_bulan
bulan=["null",
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember"
]

#data_pilihan_transfer
data_pilihan_transfer=[
    'Transfer sesama BRI','Transfer sesama BNI','Transfer sesama Mandiri','Transfer sesama BCA','Transfer sesama Bank lain'
]
#data_komisi_transfer
data_komisi_transfer=[
    '0',
    '1000',
    '3000',
    '6500',
]
#data_komisi_admin
data_komisi_admin=[
    '10000','15000','20000','25000','30000','35000','40000','45000','50000','55000','60000','65000','70000','75000','80000','85000','90000','95000','100000',
]
#Menu_bars
my_menu=Menu(root)
root.config(menu=my_menu)

file_menu=Menu(my_menu)
my_menu.add_cascade(label="FIE     ",menu=file_menu,font=("consolas",14))
file_menu.add_command(label="KOSONG...",command=our_command)
file_menu.add_separator()
file_menu.add_command(label="KOSONG...",command=our_command)

file_transfer=Menu(my_menu)
my_menu.add_cascade(label="TRANSFER     ",menu=file_transfer,font=("consolas",14))
file_transfer.add_command(label="KOSONG...",command=our_command)
file_transfer.add_separator()
file_transfer.add_command(label="KOSONG...",command=our_command)

file_tarik_tunai=Menu(my_menu)
my_menu.add_cascade(label="TARIK TUNAI     ",menu=file_tarik_tunai,font=("consolas",14))
file_tarik_tunai.add_command(label="KOSONG...",command=our_command)
file_tarik_tunai.add_separator()
file_tarik_tunai.add_command(label="KOSONG...",command=our_command)

file_jasa_link=Menu(my_menu)
my_menu.add_cascade(label="JASA LINK     ",menu=file_jasa_link,font=("consolas",14))
file_jasa_link.add_command(label="KOSONG...",command=our_command)
file_jasa_link.add_separator()
file_jasa_link.add_command(label="KOSONG...",command=our_command)

file_pembayaran=Menu(my_menu)
my_menu.add_cascade(label="PEMBAYARAN     ",menu=file_pembayaran,font=("consolas",14))
file_pembayaran.add_command(label="KOSONG...",command=our_command)
file_pembayaran.add_separator()
file_pembayaran.add_command(label="KOSONG...",command=our_command)

file_kuota=Menu(my_menu)
my_menu.add_cascade(label="KUOTA     ",menu=file_kuota,font=("consolas",14))
file_kuota.add_command(label="KOSONG...",command=our_command)
file_kuota.add_command(label="KOSONG...",command=our_command)

file_pulsa=Menu(my_menu)
my_menu.add_cascade(label="PULSA     ",menu=file_pulsa,font=("consolas",14))
file_pulsa.add_command(label="KOSONG...",command=our_command)
file_pulsa.add_command(label="KOSONG...",command=our_command)

file_accesories=Menu(my_menu)
my_menu.add_cascade(label="ACCESORIES     ",menu=file_accesories,font=("consolas",14))
file_accesories.add_command(label="KOSONG...",command=our_command)
file_accesories.add_separator()
file_accesories.add_command(label="KOSONG...",command=our_command)

#Tampilan_Judul
nomer_transaksi=Label(root,text="TRANSFER",font=("consolas",19),bg="#0a3d62",fg="#ffffff")
nomer_transaksi.place(x=100,y=20)

#Tampilan_Judul
nomer_transaksi=Label(root,text="COBET DATA MANAGEMENT",font=("consolas",19),bg="#0a3d62",fg="#ffffff")
nomer_transaksi.place(x=100,y=50)

#Tampilan_Jam
label = Label(root, font=("Consolas", 24, 'bold'), bg="#0a3d62", fg="#ffffff", bd =20)
label.place(x=85,y=80)
def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   label.config(text=text_input)
   label.after(200, digitalclock)
digitalclock()

#Tampilan_Tanggal
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
tampilan_bulan=int(now.strftime("%m"))

#Jenis_data_transfer
Jenis_transfer=Label(root,text="Jenis Data Transfer",font=("consolas",20),bg="#0a3d62",fg="#ffffff")
Jenis_transfer.place(x=1030,y=60)

#Komisi_bank
Jenis_transfer=Label(root,text="Komisi Bank",font=("consolas",20),bg="#0a3d62",fg="#ffffff")
Jenis_transfer.place(x=1000,y=200)

#Biaya_admin
Jenis_transfer=Label(root,text="Biaya Admin",font=("consolas",20),bg="#0a3d62",fg="#ffffff")
Jenis_transfer.place(x=1173,y=200)

#Nominal
Jenis_transfer=Label(root,text="Nominal",font=("consolas",20),bg="#0a3d62",fg="#ffffff")
Jenis_transfer.place(x=1128,y=358)

#Combo_box_transfer
pilihan_transfer=ttk.Combobox(root,width=25,heigh=10,values=data_pilihan_transfer,font=("consolas",18))
pilihan_transfer.current(0)
pilihan_transfer.bind("<<ComboboxSelected>>",combo_pilihan_transfer)
pilihan_transfer.place(x=1000,y=100)
#Combo_box_komisi
komisi_transfer=ttk.Combobox(root,width=11,heigh=10,values=data_komisi_transfer,font=("consolas",18))
komisi_transfer.current(0)
komisi_transfer.bind("<<ComboboxSelected>>",combo_komisi_transfer)
komisi_transfer.place(x=1000,y=250)
#Combo_biaya_admin
komisi_admin=ttk.Combobox(root,width=11,heigh=10,values=data_komisi_admin,font=("consolas",18))
komisi_admin.current(0)
komisi_admin.bind("<<ComboboxSelected>>",combo_komisi_admin)
komisi_admin.place(x=1173,y=250)

#Entry_jenis_data_transfer
entry_transfer=Text(root,height=2,width=31,font=('consolas',15))
entry_transfer.place(x=1000,y=148)
#Entry_jenis_komisi
entry_komisi=Text(root,height=2,width=15,font=('consolas',15))
entry_komisi.place(x=1000,y=300)
#Entry_biaya_admin
entry_biaya_admin=Text(root,height=2,width=15,font=('consolas',15))
entry_biaya_admin.place(x=1173,y=300)
#Entry_nominal
entry_nominal=Text(root,height=2,width=18,font=('consolas',15))
entry_nominal.place(x=1080,y=400)

#Button
hapus=Button(root,text="Hapus",relief=RAISED,font=("consolas",15),width=10,heigh=2,bg="#2f3640",command=hapus_semua)
hapus.place(x=1200,y=550)

nomer_urut_TreeView=tk.IntVar()
nomer_urut_TreeView.set
simpan=Button(root,text="Simpan",relief=RAISED,font=("consolas",15),width=10,heigh=2,bg="#2f3640",command=command_inputan)
simpan.place(x=1000,y=550)

#TreeView
my_tree = ttk.Treeview(root)
#define_our_columns
my_tree['columns']=("NO","JAM","TANGGAL","TRANSFER","SALDO KELUAR","UANG MASUK","ADMIN","KOMISI BANK")
#format our columns
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("NO",anchor=CENTER,width=50)
my_tree.column("JAM",anchor=CENTER,width=80)
my_tree.column("TANGGAL",anchor=CENTER,width=100)
my_tree.column("TRANSFER",anchor=CENTER,width=150)
my_tree.column("SALDO KELUAR",anchor=CENTER,width=100)
my_tree.column("UANG MASUK",anchor=CENTER,width=100)
my_tree.column("ADMIN",anchor=CENTER,width=100)
my_tree.column("KOMISI BANK",anchor=CENTER,width=100)
#question what is parent and what is end and index
#add_datas
my_tree.place(x=80,y=170)
#create Headings
my_tree.heading("#0",text="",anchor=CENTER)
my_tree.heading("NO",text="NO",anchor=CENTER)
my_tree.heading("JAM",text="JAM",anchor=CENTER)
my_tree.heading("TANGGAL",text="TANGGAL",anchor=CENTER)
my_tree.heading("TRANSFER",text="TRANSFER",anchor=CENTER)
my_tree.heading("SALDO KELUAR",text="SALDO KELUAR",anchor=CENTER)
my_tree.heading("UANG MASUK",text="UANG MASUK",anchor=CENTER)
my_tree.heading("ADMIN",text="ADMIN",anchor=CENTER)
my_tree.heading("KOMISI BANK",text="KOMISI BANK",anchor=CENTER)


#Copyrights
nomer_transaksi=Label(root,text="Copyright © 2020, Bogor. West Java. Indonesia. Singgih Febriana Corporation.\nAll rights reversed. Term of use | privacy policy-REVISED.\nContact Call +6285891306425.",font=("Calibri (Body)",11),bg="#0a3d62",fg="#ffffff")
nomer_transaksi.place(x=10,y=600)
tk.mainloop()
