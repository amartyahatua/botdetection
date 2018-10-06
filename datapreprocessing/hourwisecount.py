import csv
import os
import pandas as pd

class HourwiseCount: 
    def __init__(self):   
        self.created_list = list()
        self.day = list()
        self.month = list()
        self.date = list()
        self.hour = list()
        self.minute = list()
        self.second = list()
        self.year = list()
        self.tweetId = list()
        self.userID = list()
        self.df_out = []
        
        
        
        
    def unique(self,list1): 
  
        # intilize a null list 
        unique_list = [] 
        # traverse for all elements 
        for x in list1: 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 
                
        return unique_list
    
    
    
    
    
    def hourwisecount(self,path):
        dirs = os.listdir( path )
        for file in dirs:
            filename = path+file
            print(filename)
            df = pd.read_csv(filename, header=None, skiprows=1)
            self.created_list=df[1]
            self.tweetId = df[0]
            self.userID = df[8]
            
            
            
        for i in range(len(self.created_list)):
            singledata = self.created_list[i]
            self.day.append(singledata[0:3])
            self.month.append(singledata[4:7])
            self.date.append(singledata[8:10])
            self.hour.append(singledata[8:10])
            self.minute.append(singledata[11:13])
            self.second.append(singledata[14:16])
            self.year.append(singledata[26:31])
            
        
#         uniYr = self.unique(self.year)
#         uniMn = self.unique(self.month)
#         uniDt = self.unique(self.date)
#         uniHr = self.unique(self.hour)  
        
       
       
        
        out = {'Year':self.year, 'Month':self.month, 'Day':self.day, 'Date':self.date, 'Hour':self.hour}
        self.df_out = pd.DataFrame(out)
        print(self.df_out)
        
        #print(self.df_out[(self.df_out['Year'] == '2017') & (self.df_out['Month'] == 'Jul') & (self.df_out['Day'] == 'Mon') & (self.df_out['Hour'] == '24')])
        
        #print(self.df_out[(self.df_out['Year'] == '2017') & (self.df_out['Month'] == 'Jul')  & (self.df_out['Hour'] == '24')])
        
        
    def getCountHour(self, year, month, day, date, hour):
        print(self.df_out[(self.df_out['Year'] == str(year)) & (self.df_out['Month'] == str(month)) & (self.df_out['Day'] == str(day)) & (self.df_out['Date'] == str(date)) & (self.df_out['Hour'] == str(hour)) ])
        
                   
    def getCountDay(self, year, month, date, day):
        print(self.df_out[(self.df_out['Year'] == str(year)) & (self.df_out['Month'] == str(month)) & (self.df_out['Day'] == str(day)) & (self.df_out['Hour'] == str(date))])

    def getCountDate(self, year, month, date):
        print(len(self.df_out[(self.df_out['Year'] == str(year)) & (self.df_out['Month'] == str(month)) & (self.df_out['Hour'] == str(date))]))
    
    def getCountMonth(self, year, month):
        print(len(self.df_out[(self.df_out['Year'] == str(year)) & (self.df_out['Month'] == month)]))

    def getCountYear(self, year):
        print(len(self.df_out[(self.df_out['Year'] == str(year))]))

path = "\\data\\"

hwc = HourwiseCount()
hwc.hourwisecount(path)
hwc.getCountYear(2017)
hwc.getCountMonth(2017,'Jul')
hwc.getCountDate(2017,'Jul',16)
hwc.getCountDay(2017,'Jul',16,'Mon')
hwc.getCountHour(2017,'Jul',16,'Mon',24)


