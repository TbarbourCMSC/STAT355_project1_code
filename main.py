import math

import matplotlib as plt
import pandas as pd


#class (class bruh)
class bucket:
    def __init__(self,lowerBound,upperBound):
        self.lowerBound = lowerBound
        self.upperBound =  upperBound
        self.data = []

    def returnBounds(self):
        print(self.lowerBound,self.upperBound)
    
    def getLowerBound(self):
        return self.lowerBound
    def getUpperBound(self):
        return self.upperBound
    def returnData(self):
        print(self.data)

    def insert(self,data):
        self.data.append(data)
        
    #get the frequency of the data by outputting amount of data points it has
    def freqency(self):
        print(len(self.data))

#sort data into buckets
def bucketSorting(bucketList,raw_data):
    #create a dict of all the current bucket bounds
    bucket_bounds ={}
    for item in bucketList:
        bucket_bounds[item] = (item.getLowerBound(),item.getUpperBound())
    
    #iterate all the raw data and sort into proper bounds 

    #print(bucket_bounds[bound][1])
    for num in raw_data:
        for bound in bucket_bounds:
            if(num>= bucket_bounds[bound][0] and num <=bucket_bounds[bound][1]):
                bound.insert(num)
    
#calculate class width
def calculateClassWidth(data):
    #get the min and max values from the data
    min_val = min(data)
    max_val = max(data)

    class_width  =  math.ceil((max_val - min_val)/6 )
    return class_width

#generate stat_classes 
def generate_stat_classes(lowerbound,upperBound,classSize,data,width):

    class_count = 0
    #get the lowest bound use as a basis 
    base_step = min(data)
    upper_step = base_step + width - 1 

    #create the first class 
    bucket_class_list.append(bucket(base_step,upper_step))
   
    while base_step <= upperBound:
       # print("Lower bound: ",base_step)
       # print("upper bound size: ",upper_step)

        base_step =  upper_step + 1 
        upper_step += width

        bucket_class_list.append(bucket(base_step,upper_step))

#calculate class frequency

#calculate relative frequency

#calculate cumalitive frequncy 


#make a histrogram with pandas (later)

#calculate mean
def calculate_mean(raw_data):
    n_count = 0
    running_total = 0

    for item in raw_data:
        running_total+=item
        n_count+=1
    
    final_mean =  running_total/n_count
    return final_mean


#calculate median
def calculate_median(raw_data):
    #check if the data_set is even or odd 
    if((len(raw_data) + 1)  % 2 == 0):
        half_index =  int((len(raw_data) + 1)  / 2)
        half_index_plus_one = int((len(raw_data) + 1)  / 2) + 1
        return (raw_data[half_index] + raw_data[half_index_plus_one])/2
    else:
        return raw_data[15]
    
#calculate mode 



#calculate range 
def calculate_range(raw_data):
    return max(raw_data) - min(raw_data)
#calculate variance 
def calculate_variance(raw_data,mean):
    sum_total = 0
    intermediate = 0 
    count = 0 
    for data in raw_data:
        intermediate =  math.pow((data - mean),2)
        sum_total+= intermediate
        count+=1

    return sum_total/count
    
#calculate standard deviation
def calculate_standarddiv(variance):
    return math.sqrt(variance)

#calculate min 
def return_min_q(raw_data):
    return min(raw_data)

#calculate q1
def calculate_qone(raw_data):
    index = math.floor((25/100)* 30)
    return (raw_data[index]+raw_data[index +1 ])/2

#calculate Q2
def calculate_qtwo(raw_data):
    index = math.floor((50/100)* 30)
    return (raw_data[index]+raw_data[index +1 ])/2
#calculate Q3
def calculate_qthree(raw_data):
    index = math.floor((75/100)* 30)
    return (raw_data[index]+raw_data[index +1 ])/2

#calculate IQR
def calculate_iqr(q3,q1):
    return q3-q1
#calculate Max
def return_max_q(raw_data):
    return max(raw_data)
#generate box plot (pandas, later)

if __name__ == "__main__":

    raw_data_arr = []
    bucket_class_list= []
    #take in the csv file the spit out numbers 
    with open("DDr4_RAM_Latency_speeds.csv",'r') as file:
        for line in file:
            raw_data_arr = line.split(',')

    #more data cleaning
    for i in range(0,len(raw_data_arr)):
        raw_data_arr[i]= int(raw_data_arr[i])

    raw_data_arr.sort()
    print("Data before calculations:\n",raw_data_arr)

    #stat data calculations
    lowerbound =  min(raw_data_arr)
    upperbound =  max(raw_data_arr)
    #calculate the width
    class_width = calculateClassWidth(raw_data_arr)
    #generate the classes
    generate_stat_classes(lowerbound,upperbound,6,raw_data_arr,class_width)

    mean = calculate_mean(raw_data_arr)
    median = calculate_median(raw_data_arr)
    range_val = calculate_range(raw_data_arr)

    quartile_one = calculate_qone(raw_data_arr)
    quartile_two = calculate_qtwo(raw_data_arr)
    quartile_three = calculate_qthree(raw_data_arr)
    variance = calculate_variance(raw_data_arr,mean)
    standardDiv = calculate_standarddiv(variance)
    
    print("GENERATED STATS:\nMean: %d\nMedian: %d\nMode: %d\nRange: %d\nVariance: %.15f\nStandard Deviation %.15f \nQ1: %d\nQ3: %d\nIQR: %d\n" % (mean,median,23,range_val,variance,standardDiv,quartile_one,quartile_three,calculate_iqr(quartile_three,quartile_one)))
    bucketSorting(bucket_class_list,raw_data_arr)
    for item in bucket_class_list:
        print("UPPER AND LOWER BOUNDS : %d , %d" % (item.getLowerBound(),item.getUpperBound()))
        print(item.freqency())
    
    
   
    #generate graphs 
    #convert dataset into a dataframe with pandas 
    """
    dataframe = pd.DataFrame(raw_data_arr)
    boxplot = dataframe.boxplot()
    boxplot.plot()
    plt.show()
    """
    
    


    

    
    



            


   


