import csv
import os
import random
from time import sleep
from numpy import append
import error
import IRtime
import ast
class CsvList:
    def __init__(self , filename) -> None:
        self.filename = filename
        if self.file_find() == None:
            self.writer([])
    @property
    def _list(self):
        return self.reader()
    def __sub__(self , other):
        list1 = self._list
        list2 = other._list
        newlist = []
        for i in range (0, len(list1)):
            newlist.append([])
            for k in list1[i]:
                try:
                    if k in list2[i]:
                        continue
                    else:
                        newlist[i].append(k)
                except:
                    newlist[i].append(k)
                    continue
        return newlist

    def writer(self, users):
        list_csv = users 
        with open(self.filename,'w', newline='') as fill:
            writ_fill = csv.writer(fill, delimiter= ',')
            for user in list_csv:
                writ_fill.writerow(user)

    def write_column(self, lis_cloum, indexcol = 'new'):        
        acont_data1= self._list
        lenlis = []
        while len(acont_data1) < len(lis_cloum):
            acont_data1.append([])
        for i in acont_data1:
            lenlis.append(len(i))
        lenlis
        while max(lenlis) != min(lenlis):
            minindex = lenlis.index(min(lenlis))
            acont_data1[minindex].append('')
            lenlis[minindex] += 1
        if indexcol == 'new':
            for i in range (0 ,len(acont_data1)):
                acont_data1[i].append(lis_cloum[i])
        else:
            for i in range(0 ,len(acont_data1)):
                acont_data1[i][indexcol] = lis_cloum[i]
        self.writer(acont_data1)
            
    def write_row(self , lists, indexrow = 'new'):
        listall = self._list
        if indexrow == 'new':
            listall.append(lists)
        else:
            listall[indexrow] = lists
        self.writer(listall)
    def write_index(self , value , y , x):
        listall = self._list
        listall[y][x] = value
    def append_row(self , value , indexrow = -1):
        listall = self._list
        listall[indexrow].append(value)
        self.writer(listall)
    def reader(self):    
        with open(self.filename,'r') as ride:
            ride_fill = csv.reader(ride , delimiter= ',')
            lists = [user for user in ride_fill]
            return lists

    def read_row(self , row):
        listall = self.reader()
        return listall[row]
    
    def read_column(self , column):
        listall = self.reader()
        secondlist = []
        for i in range(0 , len(listall)):
            secondlist.append(listall[i][column])
        return secondlist
    def read_dict(self , y , x):
        return ast.literal_eval(self._list[y][x])

    def get_rowlist_name(self , name, index=0):
        listall = self.reader()
        for i in range(0 , len(listall)):
          if name == listall[i][index]:
              return listall[i]
        return 1

    def get_rowindex_name(self , name , index= 0):
        listall = self.reader()
        for i in range(0 , len(listall)):
            if name == listall[i][index]:
                return i

    def file_find(self,path= os.getcwd()):
        for root, dirs, files in os.walk(path):
            if self.filename in files:
                return os.path.join(root, self.filename)
    def find_by_value(self , value):
        x = None
        y = None
        for i in self._list:
            if value in i:
                y = self._list.index(i)
                x = i.index(value)
        return (y , x)
class DiscountCode:
    def __init__(self , file_buy = 'file_buy.csv' , file_invite_friends = 'file_invite_friends.csv' , file_product = 'file_product') -> None:
        self.file_buy = file_buy
        self.file_invite_friends = file_invite_friends
        self.file_product = file_product
    @property
    def buy_list(self):
        return CsvList(self.file_buy)
    @property
    def invite_frends_list(self):
        return CsvList(self.file_invite_friends)
    @property
    def product_list(self):
        pass
    def Apend_by(self , user_name ,product_code , type_buy = 'Normall' , invite_code = None ,nom_Pocket = None ):
        def _invite():
            invite_code_dict = None
            user_invite_list = []
            y , x = self.invite_frends_list.find_by_value(invite_code)
            if y == None:
                error.error_warning('this invite_code not find')
                return 1
            else:
                if nom_Pocket == None:
                    type_buy = 'invited'
                    invite_code_dict = self.invite_frends_list.read_dict(y , 1)
                    invite_code_dict['allـscore'] += 1
                    invite_code_dict['not_used_score'] +=1
                    user_invite_list  = self.invite_frends_list.read_dict(y , 3)
                    user_invite_list.append(user_name)
                else:
                    type_buy = 'use pocet'
                    invite_code_dict = self.invite_frends_list.read_dict(y , 1)
                    if invite_code_dict['not_used_score'] < nom_Pocket:
                        error.error_warning('this user Score is low')
                        return 2
                    invite_code_dict['not_used_score'] -= nom_Pocket
                    invite_code_dict['used_score'] += nom_Pocket
            self.invite_frends_list.write_index(invite_code_dict , y , 1)    
            self.invite_frends_list.write_index(str(user_invite_list) , y , 3)

        buy_info = {'date':IRtime.date() , 'hour':IRtime.hour() , 'product_code':product_code , 'type_buy': type_buy}
        y , x = self.buy_list.find_by_value(user_name)
        if x == None or y == None:
            if error.error_question('this user not find if you wand add ender y') == 1:
                if type_buy == 'Normall':
                    if error.error_question('type_buy is normall if you want to be frist_buy enter y') == 1 :
                        type_buy = 'first_buy'
                _invite()
                self.buy_list.write_row([user_name , buy_info])
                   
        else:
            _invite()
            self.buy_list.append_row(type_buy , y)
    def make_invite_code(self , user_name):
        y , x = self.invite_frends_list.find_by_value(user_name)

        pasword = ''
        datelist= [str(i) for i in ast.literal_eval(IRtime.date())]
        datestr = ''
        for i in datelist:
            datestr += i
        conter = 0
        for i in user_name:
            pasword += user_name[conter]
            conter += 2
            if conter == 8:
                conter = 1
            if conter == 9:
                break
        print(user_name , datestr)
        pasword += datestr
        code =''
        random.seed(1212)
        for i in range(0 , 10):
            code += random.choice(pasword)
        
        invite_code_dict = {'user_name':user_name,'code':code , 'date_creation':datestr , 'allـscore':0 ,'used_score':0 , 'not_used_score':0 }
        if y != None:
            print(code)
            error.error_warning('this user take code befor')
        else:
            self.invite_frends_list.write_row([user_name , invite_code_dict , code  ,[]])
