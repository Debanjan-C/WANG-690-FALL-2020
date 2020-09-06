# -*- coding: utf-8 -*-
"""Data_690_HW_2.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eAsD1QQiM3GV_v0d58SDAHLL2U7sYwrx
"""

#This list will store the users entered data
inputList = []

#This for loop will be used to prompt the user to enter 10 values.
for i in range(10):
  #The while loop will check if the case in the try statement will be true.
  while True:
      """ 
      This try case will prompt an user to enter and integer and check if it as integer. 
      The list would append it if it is an integer. It would break the loop as an integer 
      would be entered for that specific iteration.
      """
      try:
          userInput = int(input("Please enter an integer:"))
          inputList.append(userInput)
          break
      
      #The except condition will give an exception case where it will say that the value entered is not an integer
      #and will prompt the user to enter a number once again. That is why we have the "continue" term. 
      except:
          print("Enter an integer please. Examples are: 1, 2, 3..")
          continue  
print("You list of numbers are:", inputList)

"""
This method will take the user entered list in the parameter and 
try to find the largest number in the list. 
"""
def maxNumber(numList): 
  #This variable will be used to test and find the largest number.
  max = 0
  #The for loop will check each element int he list and if it is
  #larger than the value in the max value then it would store that
  #value in the max variable.
  for i in numList:
      if i > max: 
        max = i

  #prints out the maximum value.
  print("The maximum number that you entered was:", max)

"""
This method will take the user entered list in the parameter and 
try to find the smallest number in the list.
"""
def minNumber(numList): 
  """
  This variable will be used to test and find the smallest number. 
  It will initially take the lest element in the number list.
  """
  min = numList[len(numList)-1]
  """
  We use the for loop to take each data from the last element to the first
  and then we compare it with the min value. If the element is less than 
  the min value then that elements value will replace the min value.
  """
  for i in inputList[::-1]:
      if i < min: 
        min = i

  #prints the minimum value
  print("The minimum number that you entered was:", min)

"""
This method will take the largest number in the list and 
then it will subtract it by the smallest number to get the
range value.
"""
def rangeList(numList):
  #We take the range and max as a test value and set it to 0.
  range = 0
  max = 0
  # The min value is stored as the last element in numList for testing purposes.
  min = numList[len(numList)-1]
  """
  We compare each element in for loop with max value to see which one is higher
  and if a specific element is higher then we set that to the max value.
  """
  for i in numList:
      if i > max: 
        max = i
  """
  We compare each element in for loop with min value to see which one is lower
  and if a specific element is less then we set that to the min value.
  """
  for j in inputList[::-1]:
      if j < min: 
        min = j

  #The range is calculated as the max value minus the min value.
  range = max - min

  #We output the range.
  print("The range of the data you entered is:", range)

"""
This method will take the sum of all elements in the
list and divide it by the count of the elements numbers in the 
list in order to get the mean or the average. 
"""
def meanList(numList):
  #variable used as a sum variable which we will use to store the sum of each element.
  sum = 0
  #We take each element in the user entered list and add it up to find the sum of all elements.
  for i in numList:
    sum += i

  #We divide the total sum by the length or count of the the user entered list to get the mean.
  mean = sum/len(numList)

  #We output the result of the mean or the average.
  print("The mean of the data you entered is:", mean)

"""
This method is used to retrieve the standard devation of all items in the user entered list.
The formula for the standard deviation is : Square root of(sum of (each elment in list - mean of list)^2 / count or length of the list)
"""
def numStdDeviation(numList):
  sum = 0
  sumstddev = 0
  stddev = 0
  #for loop used to find the sum to retrieve the mean.
  for i in numList:
      sum += i

  #the length of the user entered list would be divided by sum to retrieve the mean
  mean = sum/len(numList)

  #this foor loop is used to find the sum of (each element in the list and subtract it by the mean)^2
  for i in numList:
      sumstddev += ((i - mean)**2)

  """
  The standard deviation is retrieved by dividing the sumstnddevaition retrieved from last 
  for loop by the count of numList and finding the square root of that value. 
  """
  stddev = (sumstddev/len(numList))**(1/2)

  #prints the standard devaiation value
  print("The standard deviation of the data you entered is:", round(stddev, 2))

"""
This method is used to retrieve the variance of all items in the user entered list. The formula for the variance is :
The square of the standard deviation. We use the same steps we used to retrieve the standard deviation in the previous 
numStdDeviation method and we retrieve the square of that. 
"""
def numVariance(numList):

  sum = 0
  sumstddev = 0
  stddev = 0 
  variance = 0
    
  #for loop used to find the sum to retrieve the mean.
  for i in numList:
      sum += i

  #the mean is the retrieved sum of the elements in the list divided by the length or count of the elements in the list.
  mean = sum/len(numList)

  #this foor loop is used to find the sum of (each element in the list and subtract it by the mean)^2
  for i in numList:
      sumstddev += ((i - mean)**2)

  """
  The standard deviation is retrieved by dividing the sumstnddevaition retrieved from last 
  for loop by the count of numList and finding the square root of that value. 
  """ 
  stddev = (sumstddev/len(numList))**(1/2)

  #The variance will be retrieved by calculating the square of the standard deviation or to the power of 2.
  variance = stddev**2

  #We print the variance and round it to the closes two decimal places.
  print("The variance of the data you entered is:", round(variance, 2))

#Calls the maxNumber method to see the maximum values entered by the user.
maxNumber(inputList)
#Calls the minNumber method to see the minimum values entered by the user.
minNumber(inputList)
#Calls the rangeList method to see the range of the values entered by the user.
rangeList(inputList)
#Calls the meanList method to see the mean of the values entered by the user.
meanList(inputList)
#Calls the numStdDeviation method to see the standard deviation of the values entered by the user.
numStdDeviation(inputList)
#Calls the numVariance method to see the variance of the values entered by the user.
numVariance(inputList)