from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror,showinfo
from calendar import Calendar
from tkcalendar import DateEntry
import datetime
import time
from random import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter.filedialog import asksaveasfilename,askopenfilename
import shutil
from PIL import Image, ImageTk
class queqe_:
      def __init__(self):
            self.queqe = []
            self.queqe.append('start')
      def append(self, x: str):
            self.queqe.append(x)
            if len(self.queqe)>2:
                  self.queqe.pop(0)

class __options__:
      def __init__(self):
            with open('options.txt', encoding = 'utf-8') as txt:
                  s = txt.read()
                  s=s.split('\n')
                  s = [x.split(' ', maxsplit = 1) for x in s]
            self.bg = s[0][1]
            self.fg = s[1][1]
            self.font1 = s[2][1]
            self.font2 = s[9][1]
            self.font3 = s[10][1]
            self.font4 = s[11][1]
            self.bg_button = s[3][1]
            self.ag = s[4][1]
            self.bg_text = s[5][1]
            self.bg_small_button = s[6][1]
            self.bg_button_galka = s[8][1]
            self.bg_calendar_button_yes = s[12][1]
            self.bg_calendar_button_no = s[13][1]
            self.ag2 = s[14][1]
            self.bg_dayoff = s[15][1]
            self.bg_yes = s[16][1]
            self.bg_no = s[17][1]

class points_:
      def __init__(self):
            self.points = 0
            with open('points.txt',encoding = 'utf-8') as txt:
                  s = txt.read()
                  self.points = int(s)
      def save(self):
            with open('points.txt', 'w' ,encoding = 'utf-8') as txt:
                  txt.write(f'{self.points}')
            return 0
      
class habit_:
      def __init__(self):
            self.list = []
            with open('habit.txt',encoding = 'utf-8') as txt:
                  s = txt.read()
                  if not s:return
                  s = s.split('\n')
                  s = [x.split('☢') for x in s]
                  s = sorted(s)
                  self.list = s
      def append(self, x):
            if x not in self.list: self.list.append(x)
            else: showerror('Ошибка','Данная привычка уже присутствует');return 1001
            self.list.sort()
            with open('habit.txt','w',encoding = 'utf-8') as txt:
                  txt.write('\n'.join(['☢'.join(x) for x in self.list]))
            showinfo('Добавление новой привычки',f'Привычка "{x[0]}" успешно добавлена')
            return 0
      def remove(self, x):
            if x in self.list: self.list.remove(x)
            else: showerror('Ошибка','Данной привычки нет в списке привычек');return 1002
            self.list.sort()
            with open('habit.txt','w',encoding = 'utf-8') as txt:
                  txt.write('\n'.join(['☢'.join(x) for x in self.list]))
            showinfo('Удаление привычки',f'Привычка {x[0]} успешно удалёна')
            return 0

class notification_:
      def __init__(self):
            self.list = []
            with open('notification.txt',encoding = 'utf-8') as txt:
                  s = txt.read()
                  if not s:return
                  s = s.split('\n')
                  s = sorted(s)
                  self.list = s
      def append(self, x):
            if x not in self.list: self.list.append(x)
            else: showerror('Ошибка','Данная привычка уже присутствует');return 1001
            self.list.sort()
            with open('notification.txt','w',encoding = 'utf-8') as txt:
                  txt.write('\n'.join([x for x in self.list]))
            showinfo('Добавление новой привычки',f'Привычка "{x}" успешно добавлена')
            return 0
      def remove(self, x):
            if x in self.list: self.list.remove(x)
            else: showerror('Ошибка','Данной привычки нет в списке');return 1002
            self.list.sort()
            with open('notification.txt','w',encoding = 'utf-8') as txt:
                  txt.write('\n'.join([x for x in self.list]))
            showinfo('Удаление привычки',f'Привычка {x} успешно удалёна')
            return 0
      
class list_habit_:
      def __init__(self):
            self.list = []
            with open('list_habit.txt',encoding = 'utf-8') as txt:
                  s = txt.read()
                  if not s:return
                  s = s.split('\n')
                  s = [x.split('☢') for x in s]
                  s = sorted(s)
                  self.list = s
      def append(self, x):
            self.list.append(x)
            self.list.sort()
            with open('list_habit.txt','w',encoding = 'utf-8') as txt:
                  txt.write('\n'.join(['☢'.join(x) for x in self.list]))
            showinfo('Добавление новой привычки',f'Запись о совершении Привычки "{x[0]}" успешно добавлена')
            return 0
      def remove(self, x):
            if x in self.list: self.list.remove(x)
            else: showerror('Ошибка','Данной записи нет в списке записей');return 1002
            self.list.sort()
            with open('list_habit.txt','w',encoding = 'utf-8') as txt:
                  txt.write('\n'.join(['☢'.join(x) for x in self.list]))
            showinfo('Удаление привычки',f'Запись о совершении Привычки {x[0]} успешно удалёна')
            return 0

class messanger_:
      def __init__(self, win):
            self.p=win
            with open('messages.txt',encoding = 'utf-8') as txt:
                  s = txt.read()
                  if not s:return
                  s = s.split('\n')
                  self.messages = s
            with open('notification.txt',encoding = 'utf-8') as txt:
                  s = txt.read()
                  self.gut_habit = []
                  if not s:return
                  s = s.split('\n')
                  s = sorted(s)
                  self.gut_habit = s
      def show(self):
            if not self.gut_habit:return
            self.win = Toplevel(self.p, bg = options.bg)
            self.win.attributes('-topmost', 1)
            self.win.attributes('-alpha', 1)
            self.win.title('Напоминание')
            #self.win.geometry('330x300+100+100')
            seed((10**18-11)*time.time()%(35742549198872617291353508656626642567))
            #print(self.gut_habit)
            mess = choice(self.messages) + '"' + choice(self.gut_habit) + '"!'
            lbl = Label(self.win, text = mess, justify="left",font = options.font3,wraplength = 300 ,bg = options.bg)
            lbl.pack()
            self.canvas = Canvas(self.win, width = 200, height = 200)
            capybaraPhoto = PhotoImage(file='kapibara_milay.png')
            self.canvas.capybaraPhoto=capybaraPhoto
            self.canvas.create_image(0,0, anchor = 'nw' , image = capybaraPhoto)
            self.canvas.pack()
            btn = Button(self.win, text = '❌',
                            fg = options.fg, bg = options.bg_dayoff,
                            font = options.font4, activebackground = options.ag,
                            command = lambda: self.win.destroy())
            btn.pack()
            self.win.after(10000, self.disapp)
      
      def disapp(self):
            alpha = self.win.attributes('-alpha')
            if alpha > 0:
                  alpha-=0.05
                  self.win.attributes('-alpha',alpha)
                  self.win.after(200, self.disapp)
            else:
                  self.win.destroy()

class note_:
      def __init__(self):
            self.list = []
            with open('note.txt',encoding = 'utf-8') as txt:
                  s = txt.read()
                  if not s:return
                  s = s.split('🐱‍🐉')
                  s = [x.split('☢') for x in s]
                  s = sorted(s)
                  self.list = s
      def append(self, x):
            if x not in self.list: self.list.append(x)
            else: showerror('Ошибка','Данная заметка уже присутствует');return 1001
            self.list.sort()
            with open('note.txt','w',encoding = 'utf-8') as txt:
                  txt.write('🐱‍🐉'.join(['☢'.join(x) for x in self.list]))
            #showinfo('Добавление новой заметки',f'Заметка {x[1]} успешно добавлена')
            return 0
      def remove(self, x):
            if x in self.list: self.list.remove(x)
            else: showerror('Ошибка','Данной заметки нет в списке заметок');return 1002
            self.list.sort()
            with open('note.txt','w',encoding = 'utf-8') as txt:
                  txt.write('🐱‍🐉'.join(['☢'.join(x) for x in self.list]))
            #showinfo('Удаление привычки',f'Запись о совершении Привычки {x[0]} успешно удалёна')
            return 0

def pass_comand():
      pass

def cbt_reg_habit():
      global win,options,queqe,canvas
      queqe.append('Регистрация привычек')
      if queqe.queqe[-2] == 'start':
            canvas.destroy()
      elif queqe.queqe[-2]=='Регистрация привычек':
            reg_habit_destroy()
      elif queqe.queqe[-2]=='Календарь привычек':
            calendar_destroy()
      elif queqe.queqe[-2]=='Заметки':
            note_destroy()
      elif queqe.queqe[-2]=='Достижения':
            achievements_destroy()
      
      reg_habit_build()

def cbt_add_add_reg_habit():
      global win, options, habit, root_add_reg_habit, entry1, cmb1
      get1 = entry1.get()
      get2 = cmb1.get()
      if not get1 or not get2:
            showerror('Ошибка','Неккоректный ввод: не введено название или тип привычки')
            return
      if get2 == '+': get2='1'
      else: get2='0'
      if not habit.append([get1, get2]): root_add_reg_habit.destroy()
      
def cbt_add_reg_habit():
      global win, options, habit, root_add_reg_habit, entry1, cmb1
      try: root_add_reg_habit.destroy()
      except:pass
      root_add_reg_habit = Toplevel(win)
      root_add_reg_habit.geometry('300x400+70+70')
      root_add_reg_habit.title('Добавление привычки')
      lbl1 = Label(root_add_reg_habit,text = 'Введите название:', bg = options.bg,
                        fg = options.fg, font = options.font1)
      lbl1.place(relx = 0, rely = 0, relwidth = 1, relheight =0.15)
      entry1 = Entry(root_add_reg_habit, bd = 3, font = options.font1)
      entry1.place(relx = 0, rely = 0.15, relwidth = 1, relheight =0.15)
      lbl2 = Label(root_add_reg_habit,text = 'Выберите вид привычки (+/-):', bg = options.bg,
                        fg = options.fg, font = options.font1)
      lbl2.place(relx = 0, rely = 0.3, relwidth = 1, relheight =0.15)
      cmb1 = ttk.Combobox(root_add_reg_habit,values = ['+','-'],state = 'readonly', font = 'Arial 28')
      cmb1.place(relx = 0, rely = 0.45, relwidth = 1, relheight =0.15)
      btn = Button(root_add_reg_habit, text = 'Добавить',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4, activebackground = options.ag,
                            command = cbt_add_add_reg_habit)
      btn.place(relx = 0.0, rely = 0.6, relwidth = 1, relheight =0.4)

def cbt_del_del_reg_habit():
      global win, options, habit, root_del_reg_habit, cmb1
      get1 = cmb1.get()
      if not get1:
            showerror('Ошибка','Неккоректный ввод: не выбрано название.')
            return
      p = get1
      for x in habit.list:
            if x[0] == get1:
                  p = x
      if not habit.remove(p):root_del_reg_habit.destroy()

def cbt_del_reg_habit():
      global win, options, habit, root_del_reg_habit, entry1, cmb1
      try: root_del_reg_habit.destroy()
      except:pass
      root_del_reg_habit = Toplevel(win)
      root_del_reg_habit.geometry('300x200+70+70')
      root_del_reg_habit.title('Удаление привычки')
      lbl1 = Label(root_del_reg_habit,text = 'Выберите название:', bg = options.bg,
                        fg = options.fg, font = options.font1)
      lbl1.place(relx = 0, rely = 0, relwidth = 1, relheight =0.3)
      cmb1 = ttk.Combobox(root_del_reg_habit,values = [x[0] for x in habit.list],state = 'readonly', font = options.font1)
      cmb1.place(relx = 0, rely = 0.3, relwidth = 1, relheight =0.3)
      btn = Button(root_del_reg_habit, text = 'Удалить',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4, activebackground = options.ag,
                            command = cbt_del_del_reg_habit)
      btn.place(relx = 0.0, rely = 0.6, relwidth = 1, relheight =0.4)
      


def reg_habit_build():
      global win, frame_reg_habit, options, habit,lbl_start
      lbl_start.config(text = 'Регистрация привычек')
      frame_reg_habit = Frame(win, bg=options.bg)
      frame_reg_habit.place(relx = 0.3, rely = 0.08, relwidth = 0.69, relheight = 0.9)
      btn_add_reg_habit = Button(frame_reg_habit, text = 'Добавить привычку',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font1, activebackground = options.ag,
                            command = cbt_add_reg_habit)
      btn_add_reg_habit.place(relx = 0.03, rely = 0.85, relwidth = 0.44, relheight =0.15)
      btn_del_reg_habit = Button(frame_reg_habit, text = 'Удалить привычку',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font1, activebackground = options.ag,
                            command = cbt_del_reg_habit)
      btn_del_reg_habit.place(relx = 0.52, rely = 0.85, relwidth = 0.44, relheight =0.15)
      lbl1 = Label(frame_reg_habit,text = 'Положительные привычки:', bg = options.bg,
                        fg = options.fg, font = options.font1, anchor = 'center')
      lbl1.place(relx = 0.03, rely = 0.0, relwidth = 0.44, relheight = 0.08)
      lbl2 = Label(frame_reg_habit,text = 'Отрицательные привычки:', bg = options.bg,
                        fg = options.fg, font = options.font1, anchor = 'center')
      lbl2.place(relx = 0.52, rely = 0.0, relwidth = 0.44, relheight = 0.08)
      frame1 = Frame(frame_reg_habit, bg=options.bg)
      frame1.place(relx = 0.03, rely = 0.1, relwidth = 0.44, relheight = 0.73)
      frame2 = Frame(frame_reg_habit, bg=options.bg)
      frame2.place(relx = 0.52, rely = 0.1, relwidth = 0.44, relheight = 0.73)
      text1 = Text(frame1, font = options.font3, wrap = 'word')
      scroll = Scrollbar(frame1,orient='vertical', command = text1.yview)
      scroll.pack(side = 'right', fill='y')
      text1.config(yscrollcommand=scroll.set)
      text1.pack()
      text1.insert(1.0, '\n'.join([f'• '+x[0] for i, x in enumerate(habit.list) if int(x[1])]))
      text1.config(state = 'disabled')
      text2 = Text(frame2, font = options.font3, wrap = 'word')
      scroll = Scrollbar(frame2,orient='vertical', command = text2.yview)
      scroll.pack(side = 'right', fill='y')
      text2.config(yscrollcommand=scroll.set)
      text2.pack()
      text2.insert(1.0, '\n'.join([f'• '+x[0] for x in habit.list if not int(x[1])]))
      text2.config(state = 'disabled')
      

def reg_habit_destroy():
      global win, frame_reg_habit
      frame_reg_habit.destroy()

def cbt_calendar():
      global win,options,queqe,canvas
      queqe.append('Календарь привычек')
      if queqe.queqe[-2] == 'start':
            canvas.destroy()
      elif queqe.queqe[-2]=='Регистрация привычек':
            reg_habit_destroy()
      elif queqe.queqe[-2]=='Календарь привычек':
            calendar_destroy()
      elif queqe.queqe[-2]=='Заметки':
            note_destroy()
      elif queqe.queqe[-2]=='Достижения':
            achievements_destroy()
      
      calendar_build()

def cbt_btn_add_add_list_habit():
      global win, options, habit,list_habit, cmb1, date_entry, lbl_points
      get1=cmb1.get()
      get2 = date_entry.get_date()
      if not get1 or not get2:
            showerror('Ошибка','Неккоректный ввод: не введено название или дата')
            return
      st = get2
      cnt = 1
      typ = 0
      for x in habit.list:
            if x[0]==get1:
                  typ=int(x[1])
                  break
      for x in list_habit.list:
            cdate = datetime.datetime.strptime(x[2], '%Y-%m-%d').date()
            if x[0]==get1 and get2-datetime.timedelta(days=7)<=cdate<=get2+datetime.timedelta(days=7):
                  cnt+=1
      ind = 5
      if cnt <= 1: ind = 5
      elif cnt == 2: ind = 6
      elif cnt == 3: ind = 6
      elif cnt == 4: ind = 7
      elif cnt == 5: ind = 7
      elif cnt == 6: ind = 8
      elif cnt == 7: ind = 8
      elif cnt == 8: ind = 9
      elif cnt == 9: ind = 9
      else: ind = 10
      points.points += (ind if typ else -ind)
      points.save()
      lbl_points.config(text = f'Баллы: {points.points}')
      list_habit.append([get1, str(typ), str(get2), str(ind)])
      root_add_list_habit.destroy()

def cbt_btn_add_list_habit(day, month, year):
      global win, options, habit,list_habit, cmb1, date_entry, root_add_list_habit
      try: root_add_list_habit.destroy()
      except: pass
      root_add_list_habit = Toplevel(win)
      root_add_list_habit.geometry('400x500+70+70')
      root_add_list_habit.title('Добавление записи о привычке')
      lbl1 = Label(root_add_list_habit,text = 'Выберите название привычки:', bg = options.bg,
                        fg = options.fg, font = options.font1)
      lbl1.place(relx = 0, rely = 0, relwidth = 1, relheight =0.15)
      cmb1 = ttk.Combobox(root_add_list_habit,values = [x[0] for x in habit.list],state = 'readonly', font = options.font1)
      cmb1.place(relx = 0, rely = 0.15, relwidth = 1, relheight =0.15)
      lbl2 = Label(root_add_list_habit,text = 'Введите дату:', bg = options.bg,
                        fg = options.fg, font = options.font1)
      lbl2.place(relx = 0, rely = 0.3, relwidth = 1, relheight =0.15)
      date_entry = DateEntry(root_add_list_habit, bd = 3, fg = options.fg, bootstyle="primary", state = 'readonly')
      date_entry.set_date(datetime.date(year, month, day))
      date_entry.place(relx = 0, rely = 0.45, relwidth = 1, relheight =0.15)

      canvas1 = Canvas(root_add_list_habit, width = 200, height = 100)
      canvas1.place(relx = 0, rely = 0.6, relwidth = 0.5, relheight = 0.2)
      capybaraPhoto = PhotoImage(file='kapibara_more2.png')
      canvas1.capybaraPhoto=capybaraPhoto
      canvas1.create_image(0,0, anchor = 'nw' , image = capybaraPhoto)
      
      canvas2 = Canvas(root_add_list_habit, width = 200, height = 100)
      canvas2.place(relx = 0.5, rely = 0.6, relwidth = 0.5, relheight = 0.2)
      capybaraPhoto = PhotoImage(file='kapibara_more.png')
      canvas2.capybaraPhoto=capybaraPhoto
      canvas2.create_image(0,0, anchor = 'nw' , image = capybaraPhoto)

      btn = Button(root_add_list_habit, text = 'Добавить!',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font1, activebackground = options.ag,
                            command = cbt_btn_add_add_list_habit)
      btn.place(relx = 0, rely = 0.8, relwidth = 1.0, relheight =0.2)

def cbt_del_del_list_habit():
      showinfo('Упс!', 'Будет добавлено позже, не укладываюсь в дедлайн😢')
      root_del_list_habit.destroy()

def cbt_btn_del_list_habit():
      global win, options, habit, list_habit,root_del_list_habit, entry1, cmb1
      try: root_del_list_habit.destroy()
      except:pass
      root_del_list_habit = Toplevel(win)
      root_del_list_habit.geometry('450x200+70+70')
      root_del_list_habit.title('Удаление привычки')
      lbl1 = Label(root_del_list_habit,text = 'Выберите запись:', bg = options.bg,
                        fg = options.fg, font = options.font1)
      lbl1.place(relx = 0, rely = 0, relwidth = 1, relheight =0.3)
      cmb1 = ttk.Combobox(root_del_list_habit,values = [f'{x[0]} ||| {x[2]}'for x in list_habit.list],state = 'readonly', font = options.font1)
      cmb1.place(relx = 0, rely = 0.3, relwidth = 1, relheight =0.3)
      btn = Button(root_del_list_habit, text = 'Удалить',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4, activebackground = options.ag,
                            command = cbt_del_del_list_habit)
      btn.place(relx = 0.0, rely = 0.6, relwidth = 1, relheight =0.4)
      
def cbt_open_grid_calendar(day,month, year):
      global win, options, habit,list_habit, root_open_calendar
      print(day, month, year)
      try: root_open_calendar.destroy()
      except: pass
      root_open_calendar = Toplevel(win, bg = options.bg)
      root_open_calendar.geometry('700x500+70+70')
      root_open_calendar.title(f'{day}-{month}-{year} Календарь привычек')
      lbl1 = Label(root_open_calendar,text = 'Положительные привычки\nза этот день:', bg = options.bg,
                        fg = options.fg, font = options.font1, anchor = 'center')
      lbl1.place(relx = 0.03, rely = 0.0, relwidth = 0.44, relheight = 0.12)
      lbl2 = Label(root_open_calendar,text = 'Отрицательные привычки\nза этот день:', bg = options.bg,
                        fg = options.fg, font = options.font1, anchor = 'center')
      lbl2.place(relx = 0.52, rely = 0.0, relwidth = 0.44, relheight = 0.12)
      frame1 = Frame(root_open_calendar, bg=options.bg)
      frame1.place(relx = 0.02, rely = 0.12, relwidth = 0.46, relheight = 0.73)
      frame2 = Frame(root_open_calendar, bg=options.bg)
      frame2.place(relx = 0.51, rely = 0.12, relwidth = 0.46, relheight = 0.73)
      text1 = Text(frame1, font = options.font3, wrap = 'word')
      scroll = Scrollbar(frame1,orient='vertical', command = text1.yview)
      scroll.pack(side = 'right', fill='y')
      text1.config(yscrollcommand=scroll.set)
      text1.pack()
      tx1 = ''
      tx2 = ''
      for x in list_habit.list:
            if x[2] == str(datetime.date(year, month, day)):
                  if int(x[1]):
                        tx1+=f'• {x[0]} — {x[3]} б.\n'
                  else:
                        tx2+=f'• {x[0]} — -{x[3]} б.\n'
      text1.insert(1.0, tx1)
      text1.config(state = 'disabled')
      text2 = Text(frame2, font = options.font3, wrap = 'word')
      scroll = Scrollbar(frame2,orient='vertical', command = text2.yview)
      scroll.pack(side = 'right', fill='y')
      text2.config(yscrollcommand=scroll.set)
      text2.pack()
      text2.insert(1.0, tx2)
      text2.config(state = 'disabled')
      cbt_btn_add_list_habit2 = lambda d = day, m = month, y = year: cbt_btn_add_list_habit(d,m,y)
      btn_add_list_habit = Button(root_open_calendar, text = 'Добавить запись',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font1, activebackground = options.ag,
                            command = cbt_btn_add_list_habit2)
      btn_add_list_habit.place(relx = 0.02, rely = 0.85, relwidth = 0.46, relheight =0.15)
      btn_del_list_habit = Button(root_open_calendar, text = 'Удалить запись',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font1, activebackground = options.ag,
                            command = cbt_btn_del_list_habit)
      btn_del_list_habit.place(relx = 0.51, rely = 0.85, relwidth = 0.46, relheight =0.15)

def grid_calendar_build():
      global win, frame_calendar, options, habit,lbl_start,list_habit ,entry_month, entry_year, frame_grid_calendar
      frame_grid_calendar = Frame(frame_calendar, bg=options.bg)
      frame_grid_calendar.place(relx = 0, rely = 0.1, relwidth = 1, relheight = 0.9)
      month = int(entry_month.get())
      year = int(entry_year.get())
      clnd = Calendar().monthdatescalendar(year,month)
      mp = {}
      for i in list_habit.list:
            mp[i[2]]=0
      #print(list_habit.list)
      for i in list_habit.list:
            #print(i)
            mp[i[2]]+= (1 if int(i[1]) else -1)
      for i in range(len(clnd)):
            frame_grid_calendar.grid_rowconfigure(i, weight = 1)
            for j in range(len(clnd[i])):
                  #cbt_open_grid_calendar2 = lambda: cbt_open_grid_calendar(clnd[i][j].day,clnd[i][j].month,clnd[i][j].year)
                  btn = Button(frame_grid_calendar, text = clnd[i][j].day,
                            fg = options.fg, bg = ((options.bg_calendar_button_yes if j < 5 else options.bg_dayoff) if clnd[i][j].month == month else options.bg_calendar_button_no) if str(clnd[i][j]) not in mp else (options.bg_yes if mp[str(clnd[i][j])] >= 0 else options.bg_no) , 
                            font = options.font4, activebackground = options.ag2,
                            command =lambda day=clnd[i][j].day, month=clnd[i][j].month, year=clnd[i][j].year: cbt_open_grid_calendar(day, month, year))
                  btn.grid(row = i,column = j, sticky='WENS')
                  frame_grid_calendar.grid_columnconfigure(j, weight = 1)
      
def grid_calendar_destroy():
      frame_grid_calendar.destroy()

def cbt_btn_back():
      global win, frame_calendar, options, habit,lbl_start, entry_month, entry_year
      get1 = int(entry_month.get())
      get2 = int(entry_year.get())
      entry_month.config(state='normal')
      entry_year.config(state='normal')
      get1-=1
      if not get1:
            get1 = 12
            get2 -= 1
      entry_month.delete(0, 'end')
      entry_year.delete(0, 'end')
      entry_month.insert(0, get1)
      entry_year.insert(0, get2)
      entry_month.config(state='disabled')
      entry_year.config(state='disabled')
      grid_calendar_destroy()
      grid_calendar_build()
      
def cbt_btn_forward():
      global win, frame_calendar, options, habit,lbl_start, entry_month, entry_year
      get1 = int(entry_month.get())
      get2 = int(entry_year.get())
      entry_month.config(state='normal')
      entry_year.config(state='normal')
      get1+=1
      if get1==13:
            get1 = 1
            get2 += 1
      entry_month.delete(0, 'end')
      entry_year.delete(0, 'end')
      entry_month.insert(0, get1)
      entry_year.insert(0, get2)
      entry_month.config(state='disabled')
      entry_year.config(state='disabled')
      grid_calendar_destroy()
      grid_calendar_build()

def cbt_btn_create_report():
      global win, options, habit, list_habit, root_report, fig, ax, canvas, text_report, date_entry1, date_entry2
      date1 = date_entry1.get_date()
      date2 = date_entry2.get_date()

      if date1>date2:
            showerror('Ошибка','Начальная дата больше конечной!')
            return
      habit_cnt = {}
      habit_type = {}
      for x in habit.list:
            habit_cnt[x[0]]=0
            habit_type[x[0]]=int(x[1])
      for x in list_habit.list:
            cdate = datetime.datetime.strptime(x[2], '%Y-%m-%d').date()
            if date1<=cdate<=date2:
                  habit_cnt[x[0]]+=1
      ax.clear()
      habit_val = sorted(sorted(list(habit_cnt.keys()), key = lambda x: habit_cnt[x])[-20:])#[::-1]
      if sum(list(habit_cnt.values()))>0:
            col = []
            for x in habit_val:
                  if habit_type[x]:
                        col.append('green')
                  else:
                        col.append('red')
            bars = ax.bar(habit_val,[habit_cnt[x] for x in habit_val], color = col, edgecolor = options.fg, linewidth = 0.5)
            for x in bars:
                  h = x.get_height()
                  if h > 0:
                        ax.text(x.get_x()+x.get_width()/2, h+0.05, f'{int(h)}', ha = 'center', va = 'bottom', fontweight = options.fg, fontsize = 9, color = 'MidnightBlue')
            ax.set_title(f'Количество выполненных привычек\nс {date1} до {date2}', fontsize = 12, fontweight = 'bold', color = options.fg, pad = 15)
            ax.set_xlabel('Привычки', color = options.fg, fontsize=11, labelpad = 10)
            ax.set_ylabel('Количество', color = options.fg, fontsize=11, labelpad = 10)

            ax.set_xticklabels(habit_val, rotation = 45, ha = 'right', fontsize = 9)
            ax.tick_params(axis='x', colors = options.fg)
            ax.tick_params(axis='y', colors = options.fg)
            ax.grid(1, axis='y', linestyle = '--', alpha = 0.3)
            fig.tight_layout()
      else:
            ax.set_title('Выберите даты и нажмите "Создать отчёт"', 
                 fontsize=12, fontweight='bold', color=options.fg, pad=15)
            ax.grid(1, axis='y', linestyle='--', alpha=0.3)
      canvas.draw()

      text_report.config(state='normal')
      text_report.delete('1.0', 'end')
      tx = f'Отчёт по прогрессу (о количестве выполнений)\nПо периоду {date1} — {date2}\n'
      habit_val = sorted(list(habit_cnt.keys()), key = lambda x: habit_cnt[x])
      habit_val = [x for x in habit_val if habit_cnt[x]]
      tx1='\nПоложительные привычки:\n'
      tx2='\nОтрицательные привычки:\n'
      c1,c2 = 0, 0
      for i in habit_val[::-1]:
            if habit_type[i]:
                  tx1+=f'• {i} {habit_cnt[i]}\n'
                  c1+=habit_cnt[i]
            else:
                  tx2+=f'• {i} {habit_cnt[i]}\n'
                  c2+=habit_cnt[i]
      tx+=tx1
      tx+=tx2
      tx+=f'\nВсего совершено положительных привычек: {c1}\nВсего совершено отрицательных привычек: {c2}'
      text_report.insert('1.0', tx)
      text_report.config(state = 'disabled')
            
def cbt_btn_report():
      global win, options, habit, list_habit, root_report, fig, ax, canvas, text_report, date_entry1, date_entry2
      try: root_report.destroy()
      except: pass
      root_report = Toplevel(win, bg = options.bg)
      root_report.geometry('800x550+70+70')
      root_report.title(f'Отчёт по прогрессу')
      lbl1 = Label(root_report,text = 'Начальная дата:', bg = options.bg,
                        fg = options.fg, font = options.font1, anchor = 'w')
      lbl1.place(relx = 0.01, rely = 0.01, relwidth = 0.21, relheight = 0.08)
      lbl2 = Label(root_report,text = 'Конечная дата:', bg = options.bg,
                        fg = options.fg, font = options.font1, anchor = 'w')
      lbl2.place(relx = 0.34, rely = 0.01, relwidth = 0.20, relheight = 0.08)
      date_entry1 = DateEntry(root_report, bd = 3, fg = options.fg, bootstyle="primary", state = 'readonly')
      date_entry1.place(relx = 0.23, rely = 0.01, relwidth = 0.1, relheight =0.08)
      date_entry2 = DateEntry(root_report, bd = 3, fg = options.fg, bootstyle="primary", state = 'readonly')
      date_entry2.place(relx = 0.55, rely = 0.01, relwidth = 0.1, relheight =0.08)
      btn_create_report =  Button(root_report, text = 'Создать',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font1, activebackground = options.ag,
                            command = cbt_btn_create_report)
      btn_create_report.place(relx = 0.66, rely = 0.005, relwidth = 0.33, relheight =0.08)
      frame_text = Frame(root_report, bg=options.bg)
      frame_text.place(relx = 0.01, rely = 0.1, relwidth = 0.48, relheight = 0.89)
      frame_grafik = Frame(root_report, bg=options.bg)
      frame_grafik.place(relx = 0.51, rely = 0.1, relwidth = 0.48, relheight = 0.89)
      text_report = Text(frame_text, font = options.font3, wrap = 'word', height = 30)
      scroll = Scrollbar(frame_text,orient='vertical', command = text_report.yview)
      scroll.pack(side = 'right', fill='y')
      text_report.config(yscrollcommand=scroll.set)
      text_report.pack()
      text_report.config(state = 'disabled')
      
      fig = Figure(figsize=(7, 5), dpi=80, facecolor=options.bg)
      ax = fig.add_subplot(111)
      ax.set_facecolor(options.bg)
      ax.set_title('Выберите даты и нажмите "Создать отчёт"', 
                 fontsize=12, fontweight='bold', color=options.fg, pad=15)
      ax.grid(True, axis='y', linestyle='--', alpha=0.3)
      canvas = FigureCanvasTkAgg(fig, master=frame_grafik)
      canvas.draw()
      canvas_widget = canvas.get_tk_widget()
      canvas_widget.pack(fill='both', expand=True, padx=5, pady=5)


def calendar_build():
      global win, frame_calendar, options, habit,lbl_start, entry_month, entry_year
      lbl_start.config(text = 'Календарь привычек')
      frame_calendar = Frame(win, bg=options.bg)
      frame_calendar.place(relx = 0.3, rely = 0.08, relwidth = 0.69, relheight = 0.9)
      entry_month = Entry(frame_calendar, bd = 3, font = options.font1,justify='center')
      entry_month.place(relx = 0.13, rely = 0.005, relwidth = 0.1, relheight =0.09)
      entry_month.insert(0, datetime.datetime.today().month)
      entry_month.config(state='disabled')
      entry_year = Entry(frame_calendar, bd = 3, font = options.font1,justify='center')
      entry_year.place(relx = 0.23, rely = 0.005, relwidth = 0.1, relheight =0.09)
      entry_year.insert(0, datetime.datetime.today().year)
      entry_year.config(state='disabled')
      lbl = Label(frame_calendar,text = 'Месяц:', bg = options.bg,
                        fg = options.fg, font = options.font1, anchor = 'w')
      lbl.place(relx = 0.0, rely = 0, relwidth = 0.13, relheight = 0.1)
      btn_back = Button(frame_calendar, text = '<',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4, activebackground = options.ag,
                            command = cbt_btn_back)
      btn_back.place(relx = 0.8, rely = 0.005, relwidth = 0.1, relheight =0.09)
      btn_forward = Button(frame_calendar, text = '>',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4, activebackground = options.ag,
                            command = cbt_btn_forward)
      btn_forward.place(relx = 0.9, rely = 0.005, relwidth = 0.1, relheight =0.09)
      btn_report = Button(frame_calendar, text = 'Отчёт по прогрессу',
                            fg = options.fg, bg = options.bg_button_galka,
                            font = options.font1, activebackground = options.ag,
                            command = cbt_btn_report)
      btn_report.place(relx = 0.38, rely = 0.005, relwidth = 0.4, relheight =0.09)
      grid_calendar_build()
      

def calendar_destroy():
      frame_calendar.destroy()

def cbt_note():
      global win,options,queqe,canvas
      queqe.append('Заметки')
      if queqe.queqe[-2] == 'start':
            canvas.destroy()
      elif queqe.queqe[-2]=='Регистрация привычек':
            reg_habit_destroy()
      elif queqe.queqe[-2]=='Календарь привычек':
            calendar_destroy()
      elif queqe.queqe[-2]=='Заметки':
            note_destroy()
      elif queqe.queqe[-2]=='Достижения':
            achievements_destroy()
      
      note_build()

def cbt_btn_clk():
      global win, frame_note, options, habit,lbl_start, entry1, text_add_note, entry2
      s = askopenfilename()
      entry2.config(state = 'normal')
      entry2.delete(0, 'end')
      entry2.insert(0, s)
      #entry2.config(state = 'disabled')

def replaced(s):
      for i in '/\:*?"<>|.':
            s=s.replace(i,'')
      return s

def cbt_btn_add_add_note():
      global win, frame_note, options, habit,lbl_start, entry1, text_add_note, entry2, note, root_add_note
      get1 = entry1.get()
      get2 = text_add_note.get(1.0, 'end')
      if not get1:showerror('Ошибка','Не введено название');return
      get3 = entry2.get()
      date = datetime.datetime.today()
      name = f'{get1} {date}'
      name=replaced(name)
      name_images =  ''
      if get3:
            try:
                  shutil.copy(get3, 'images/'+name+'.'+get3.split('.')[-1])
                  name_images =  'images/'+name+'.'+get3.split('.')[-1]
            except Exception as e:
                  showerror('Ошибка','Исходный файл не найден')
                  print(e)
                  return
      str_date = str(date)
      note.append([str_date[:str_date.rfind('.')], get1, get2, name_images])
      #print(note.list)
      showinfo('Успех!','Заметка успешно добавлена!')
      root_add_note.destroy()
      
def cbt_btn_add_note():
      global win, frame_note, options, habit,lbl_start, entry1, text_add_note, entry2, root_add_note
      try: root_add_note.destroy()
      except: pass
      root_add_note = Toplevel(win, bg = options.bg)
      root_add_note.geometry('400x500+70+20')
      root_add_note.title('Добавление заметки')
      lbl1 = Label(root_add_note,text = 'Название:', bg = options.bg,
                        fg = options.fg, font = options.font1)
      lbl1.place(relx = 0, rely = 0, relwidth = 1, relheight =0.08)
      entry1 = Entry(root_add_note, bd = 3, font = options.font1)
      entry1.place(relx = 0.0, rely = 0.08, relwidth = 1, relheight =0.1)
      lbl2 = Label(root_add_note,text = 'Текст заметки:', bg = options.bg,
                        fg = options.fg, font = options.font1)
      lbl2.place(relx = 0, rely = 0.18, relwidth = 1, relheight =0.08)
      frame_text = Frame(root_add_note, bg=options.bg)
      frame_text.place(relx = 0, rely = 0.26, relwidth = 1, relheight = 0.5)
      text_add_note = Text(frame_text, font = options.font3, wrap = 'word', height = 30)
      scroll = Scrollbar(frame_text,orient='vertical', command = text_add_note.yview)
      scroll.pack(side = 'right', fill='y')
      text_add_note.config(yscrollcommand=scroll.set)
      text_add_note.pack()
      entry2 = Entry(root_add_note, bd = 3, font = options.font1, state='disabled')
      entry2.place(relx = 0.0, rely = 0.76, relwidth = 0.9, relheight =0.1)
      btn_clk = Button(root_add_note, text = '✔',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4, activebackground = options.ag,
                            command = cbt_btn_clk)
      btn_clk.place(relx = 0.9, rely = 0.76, relwidth = 0.1, relheight =0.1)
      btn_add = Button(root_add_note, text = 'Добавить',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font3, activebackground = options.ag,
                            command = cbt_btn_add_add_note)
      btn_add.place(relx = 0, rely = 0.86, relwidth = 1, relheight =0.14)

def cbt_del_del_note():
      global win, options, note, root_del_note, cmb1
      get = cmb1.get()
      if not get:
            showerror('Ошибка','Неккоректный ввод: не выбрана заметка.')
            return
      i = get.rfind(' Дата: ')
      a = get[:i]
      b = get[i+7:]
      p = []
      for i in note.list:
            if b in i[0] and a == i[1]:
                  p = i
      if not note.remove(p):root_del_note.destroy();showinfo('Удаление заметки','Заметка удалена успешно')

def cbt_btn_del_note():
      global win, options, note, root_del_note, cmb1
      try: root_del_note.destroy()
      except:pass
      root_del_note = Toplevel(win)
      root_del_note.geometry('300x200+70+70')
      root_del_note.title('Удаление заметки')
      lbl1 = Label(root_del_note,text = 'Выберите:', bg = options.bg,
                        fg = options.fg, font = options.font1)
      lbl1.place(relx = 0, rely = 0, relwidth = 1, relheight =0.3)
      cmb1 = ttk.Combobox(root_del_note,values = [x[1]+' Дата: ' + x[0] for x in note.list],state = 'readonly', font = options.font1)
      cmb1.place(relx = 0, rely = 0.3, relwidth = 1, relheight =0.3)
      btn = Button(root_del_note, text = 'Удалить',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4, activebackground = options.ag,
                            command = cbt_del_del_note)
      btn.place(relx = 0.0, rely = 0.6, relwidth = 1, relheight =0.4)
      
def cbt_btn_click():
      global win, frame_note, options, habit,lbl_start, note, text_note, cmb, canvas_note
      get = cmb.get()
      if not get:return
      i = get.rfind(' Дата: ')
      a = get[:i]
      b = get[i+7:]
      p = []
      for i in note.list:
            if b in i[0] and a == i[1]:
                  p = i
      text_note.delete(1.0, 'end')
      text_note.insert(1.0, p[1]+'\n\n'+p[2])
      if p[3]:
            try:
                  canvas_width = canvas_note.winfo_width()
                  canvas_height = canvas_note.winfo_height()
                  image = Image.open(p[3])
                  image_width, image_height = image.size
                  k = min(canvas_width/image_width,canvas_height/image_height)
                  image = image.resize((int(image_width*k), int(image_height*k)),Image.Resampling.LANCZOS)
                  image_tk = ImageTk.PhotoImage(image)
                  canvas_note.image_tk = image_tk
                  canvas_note.delete('all')
                  canvas_note.create_image(0,0,anchor='nw', image = image_tk)
            except Exception as e:print(e)
      else:
            canvas_note.delete('all')
                  
def note_build():
      global win, frame_note, options, habit,lbl_start, note, text_note, cmb, canvas_note
      lbl_start.config(text = 'Заметки')
      frame_note = Frame(win, bg=options.bg)
      frame_note.place(relx = 0.3, rely = 0.08, relwidth = 0.69, relheight = 0.9)
      btn_add_note = Button(frame_note, text = '+',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4, activebackground = options.ag,
                            command = cbt_btn_add_note)
      btn_add_note.place(relx = 0.01, rely = 0.01, relwidth = 0.08, relheight =0.08)
      btn_del_note = Button(frame_note, text = '-',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4, activebackground = options.ag,
                            command = cbt_btn_del_note)
      btn_del_note.place(relx = 0.11, rely = 0.01, relwidth = 0.08, relheight =0.08)
      
      cmb = ttk.Combobox(frame_note,values = [x[1]+' Дата: ' + x[0] for x in note.list],state = 'readonly', font = options.font1)
      cmb.place(relx = 0.2, rely = 0.01, relwidth = 0.6, relheight =0.08)

      frame_text = Frame(frame_note, bg=options.bg)
      frame_text.place(relx = 0, rely = 0.1, relwidth = 0.5, relheight = 0.9)
      text_note = Text(frame_text, font = options.font3, wrap = 'word', height = 30)
      scroll = Scrollbar(frame_text,orient='vertical', command = text_note.yview)
      scroll.pack(side = 'right', fill='y')
      text_note.config(yscrollcommand=scroll.set)
      text_note.pack()

      canvas_note = Canvas(frame_note, bg = options.bg)
      canvas_note.place(relx = 0.5, rely = 0.1, relwidth = 0.5, relheight = 0.9)
      
      btn_click = Button(frame_note, text = 'Посмотреть',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font1, activebackground = options.ag,
                            command = cbt_btn_click)
      btn_click.place(relx = 0.8, rely = 0.01, relwidth = 0.2, relheight =0.08)

      
def note_destroy():
      frame_note.destroy()

def cbt_achievements():
      global win,options,queqe,canvas
      queqe.append('Достижения')
      if queqe.queqe[-2] == 'start':
            canvas.destroy()
      elif queqe.queqe[-2]=='Регистрация привычек':
            reg_habit_destroy()
      elif queqe.queqe[-2]=='Календарь привычек':
            calendar_destroy()
      elif queqe.queqe[-2]=='Заметки':
            note_destroy()
      elif queqe.queqe[-2]=='Достижения':
            achievements_destroy()
      
      achievements_build()

def cbt_btn_add_notification():
      global win, frame_achievements, options, habit, list_habit, lbl_start, text_notification, cmb_notification
      get = cmb_notification.get()
      if not get: showerror('Ошибка', 'Не выбрано')
      notification.append(get)
      print(notification.list)
      text_notification.config(state='normal')
      text_notification.delete(1.0, 'end')
      tx = 'Уведомления включены по:\n'+'\n'.join([x for x in notification.list])
      text_notification.insert(1.0, tx)
      text_notification.config(state='disabled')

def cbt_btn_del_notification():
      global win, frame_achievements, options, habit, list_habit, lbl_start, text_notification, cmb_notification
      get = cmb_notification.get()
      if not get: showerror('Ошибка', 'Не выбрано')
      notification.remove(get)
      text_notification.config(state='normal')
      text_notification.delete(1.0, 'end')
      tx = 'Уведомления включены по:\n'+'\n'.join([x for x in notification.list])
      text_notification.insert(1.0, tx)
      text_notification.config(state='disabled')

def achievements_build():
      global win, frame_achievements, options, habit, list_habit, lbl_start, text_notification, cmb_notification
      lbl_start.config(text = 'Достижения')
      frame_achievements = Frame(win, bg=options.bg)
      frame_achievements.place(relx = 0.3, rely = 0.1, relwidth = 0.69, relheight = 0.9)
      lbl = Label(frame_achievements,text = 'Ваши Достижения:', bg = options.bg,
                        fg = options.fg, font = options.font1, anchor = 'center', justify = 'center')
      lbl.place(relx = 0.0, rely = 0, relwidth = 0.5, relheight = 0.1)   
      lbl = Label(frame_achievements,text = 'Уведомления:', bg = options.bg,
                        fg = options.fg, font = options.font1, anchor = 'center', justify = 'center')
      lbl.place(relx = 0.5, rely = 0, relwidth = 0.5, relheight = 0.1)     
      frame_text = Frame(frame_achievements, bg=options.bg)
      frame_text.place(relx = 0, rely = 0.1, relwidth = 0.5, relheight = 0.9)
      text_achievements = Text(frame_text, font = 'Arial 11', wrap = 'word', height = 30)
      scroll = Scrollbar(frame_text,orient='vertical', command = text_achievements.yview)
      scroll.pack(side = 'right', fill='y')
      text_achievements.config(yscrollcommand=scroll.set)
      text_achievements.pack()
      tx = 'Набрано баллов:\n'
      cnt1, cnt2, cnt3, cnt4,cnt, cnt5 = 0,0,0,0,0, 0
      p = [[y for y in x] for x in list_habit.list]
      for i in range(len(p)):
            p[i][2] = datetime.datetime.strptime(p[i][2], '%Y-%m-%d').date()
      p = sorted(p, key = lambda x: [x[2], x[0]], reverse=1)
      for i in list_habit.list:
            cdate = datetime.datetime.strptime(i[2], '%Y-%m-%d').date()
            date_today = datetime.datetime.today().date()
            if cdate == date_today:cnt1+=int(i[3]) if int(i[1]) else -int(i[3])
            if cdate == date_today-datetime.timedelta(days=1):cnt2+=int(i[3]) if int(i[1]) else -int(i[3])
            if cdate.isocalendar()[1] == date_today.isocalendar()[1] and cdate.year == date_today.year: cnt3+=int(i[3]) if int(i[1]) else -int(i[3])
            if cdate.year == date_today.year:cnt4+=int(i[3]) if int(i[1]) else -int(i[3])
            if cdate.year == date_today.year and cdate.month == date_today.month: cnt5+=int(i[3]) if int(i[1]) else -int(i[3])            
            cnt+=int(i[3]) if int(i[1]) else -int(i[3])
      tx+=f'За сегодня – {cnt1},\nЗа вчера – {cnt2},\nЗа неделю – {cnt3},\nЗа текущий месяц – {cnt5},\nЗа текущий год – {cnt4},\nВсего – {cnt}.\n'
      tx+= '\nДетализация достижений по дням:\n'
      for i in p: tx += f'{i[2]} {i[0]} – {i[3] if int(i[1]) else -int(i[3])} б.,\n'
      text_achievements.insert(1.0, tx)
      text_achievements.config(state='disabled')
      frame_notification = Frame(frame_achievements, bg=options.bg)
      frame_notification.place(relx = 0.5, rely = 0.1, relwidth = 0.5, relheight = 0.7)
      text_notification = Text(frame_notification, font = options.font3, wrap = 'word', height = 30)
      scroll = Scrollbar(frame_text,orient='vertical', command = text_notification.yview)
      scroll.pack(side = 'right', fill='y')
      text_notification.config(yscrollcommand=scroll.set)
      text_notification.pack()
      tx = 'Уведомления включены по:\n'+'\n'.join([x for x in notification.list])
      text_notification.insert(1.0, tx)
      text_notification.config(state='disabled')
      print(habit.list)
      cmb_notification = ttk.Combobox(frame_achievements,values = [x[0] for x in habit.list if int(x[1])],state = 'readonly', font = options.font1)
      cmb_notification.place(relx = 0.5, rely = 0.8, relwidth = 0.5, relheight =0.1)
      btn_add_notification = Button(frame_achievements, text = '+',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4,activebackground = options.ag,
                            command = cbt_btn_add_notification)
      btn_add_notification.place(relx = 0.5, rely = 0.9, relwidth = 0.25, relheight =0.1)
      btn_del_notification = Button(frame_achievements, text = '-',
                            fg = options.fg, bg = options.bg_small_button,
                            font = options.font4,activebackground = options.ag,
                            command = cbt_btn_del_notification)
      btn_del_notification.place(relx = 0.75, rely = 0.9, relwidth = 0.25, relheight =0.1)

      
      
def achievements_destroy():
      frame_achievements.destroy()

def start():
      global win,options,queqe,points,habit, btn_reg_habit, btn_calendar,list_habit,\
             btn_note, btn_achievements, canvas, lbl_start, lbl_points, note, notification
      queqe = queqe_()
      options = __options__()
      points = points_()
      habit = habit_()
      list_habit = list_habit_()
      note = note_()
      notification = notification_()
      win = Tk()
      win.title('Трекер привычек')
      win.geometry('1000x600+50+50')
      win.config(bg = options.bg)
      btn_reg_habit = Button(win, text = 'Регистрация привычек',
                            fg = options.fg, bg = options.bg_button,
                            font = options.font1, activebackground = options.ag,
                            command = cbt_reg_habit)
      btn_reg_habit.place(relx = 0.025, rely = 0.08, relwidth = 0.25, relheight =0.2)
      btn_calendar= Button(win, text = 'Календарь привычек',
                            fg = options.fg, bg = options.bg_button,
                            font = options.font1,activebackground = options.ag,
                            command = cbt_calendar)
      btn_calendar.place(relx = 0.025, rely = 0.3, relwidth = 0.25, relheight =0.2)
      btn_note = Button(win, text = 'Заметки',
                            fg = options.fg, bg = options.bg_button,
                            font = options.font1,activebackground = options.ag,
                            command = cbt_note)
      btn_note.place(relx = 0.025, rely = 0.52, relwidth = 0.25, relheight =0.2)
      btn_achievements = Button(win, text = 'Достижения и\n Уведомления',
                            fg = options.fg, bg = options.bg_button,
                            font = options.font1,activebackground = options.ag,
                            command = cbt_achievements)
      btn_achievements.place(relx = 0.025, rely = 0.74, relwidth = 0.25, relheight =0.2)

      canvas = Canvas(win, bg = 'white')
      canvas.place(relx = 0.3, rely = 0.08, relwidth = 0.69, relheight = 0.9)
      capybaraPhoto = PhotoImage(file='kapibara2.png')
      canvas.create_image(0,0, anchor = 'nw', image = capybaraPhoto)

      lbl_start = Label(win,text = 'Трекер привычек от Pythonja10', bg = options.bg,
                        fg = options.fg, font = options.font2, anchor = 'w')
      lbl_start.place(relx = 0.025, rely = 0, relwidth = 0.8, relheight = 0.08)

      lbl_points = Label(win,text = f'Баллы: {points.points}', bg = options.bg,
                        fg = options.fg, font = options.font2, anchor = 'e')
      lbl_points.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 0.08)

      messanger = messanger_(win)
      messanger.show()
      
      win.mainloop()

if __name__ == '__main__':
      start()

