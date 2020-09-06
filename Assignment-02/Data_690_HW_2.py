{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Data_690_HW_2.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyN33sFLdEwjdyHS4xF38fxx",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Debanjan-C/WANG-690-FALL-2020/blob/master/Assignment-02/Data_690_HW_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w4QKNCNLDpvL",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "outputId": "afc2d896-6da4-4724-f3a8-ac1b81630ddd"
      },
      "source": [
        "#This list will store the users entered data\n",
        "inputList = []\n",
        "\n",
        "#This for loop will be used to prompt the user to enter 10 values.\n",
        "for i in range(10):\n",
        "  #The while loop will check if the case in the try statement will be true.\n",
        "  while True:\n",
        "      \"\"\" \n",
        "      This try case will prompt an user to enter and integer and check if it as integer. \n",
        "      The list would append it if it is an integer. It would break the loop as an integer \n",
        "      would be entered for that specific iteration.\n",
        "      \"\"\"\n",
        "      try:\n",
        "          userInput = int(input(\"Please enter an integer:\"))\n",
        "          inputList.append(userInput)\n",
        "          break\n",
        "      \n",
        "      #The except condition will give an exception case where it will say that the value entered is not an integer\n",
        "      #and will prompt the user to enter a number once again. That is why we have the \"continue\" term. \n",
        "      except:\n",
        "          print(\"Enter an integer please. Examples are: 1, 2, 3..\")\n",
        "          continue  \n",
        "print(\"You list of numbers are:\", inputList)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Please enter an integer:w\n",
            "Enter an integer please. Examples are: 1, 2, 3..\n",
            "Please enter an integer:23\n",
            "Please enter an integer:12\n",
            "Please enter an integer:5432\n",
            "Please enter an integer:643\n",
            "Please enter an integer:23\n",
            "Please enter an integer:12\n",
            "Please enter an integer:4.5\n",
            "Enter an integer please. Examples are: 1, 2, 3..\n",
            "Please enter an integer:43\n",
            "Please enter an integer:154\n",
            "Please enter an integer:64\n",
            "Please enter an integer:345\n",
            "You list of numbers are: [23, 12, 5432, 643, 23, 12, 43, 154, 64, 345]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OsUNj1wzCXn6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\"\"\"\n",
        "This method will take the user entered list in the parameter and \n",
        "try to find the largest number in the list. \n",
        "\"\"\"\n",
        "def maxNumber(numList): \n",
        "  #This variable will be used to test and find the largest number.\n",
        "  max = 0\n",
        "  #The for loop will check each element int he list and if it is\n",
        "  #larger than the value in the max value then it would store that\n",
        "  #value in the max variable.\n",
        "  for i in numList:\n",
        "      if i > max: \n",
        "        max = i\n",
        "\n",
        "  #prints out the maximum value.\n",
        "  print(\"The maximum number that you entered was:\", max)\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eSKgK6zVCcCH",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\"\"\"\n",
        "This method will take the user entered list in the parameter and \n",
        "try to find the smallest number in the list.\n",
        "\"\"\"\n",
        "def minNumber(numList): \n",
        "  \"\"\"\n",
        "  This variable will be used to test and find the smallest number. \n",
        "  It will initially take the lest element in the number list.\n",
        "  \"\"\"\n",
        "  min = numList[len(numList)-1]\n",
        "  \"\"\"\n",
        "  We use the for loop to take each data from the last element to the first\n",
        "  and then we compare it with the min value. If the element is less than \n",
        "  the min value then that elements value will replace the min value.\n",
        "  \"\"\"\n",
        "  for i in inputList[::-1]:\n",
        "      if i < min: \n",
        "        min = i\n",
        "\n",
        "  #prints the minimum value\n",
        "  print(\"The minimum number that you entered was:\", min)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GOOaU9xMCdps",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\"\"\"\n",
        "This method will take the largest number in the list and \n",
        "then it will subtract it by the smallest number to get the\n",
        "range value.\n",
        "\"\"\"\n",
        "def rangeList(numList):\n",
        "  #We take the range and max as a test value and set it to 0.\n",
        "  range = 0\n",
        "  max = 0\n",
        "  # The min value is stored as the last element in numList for testing purposes.\n",
        "  min = numList[len(numList)-1]\n",
        "  \"\"\"\n",
        "  We compare each element in for loop with max value to see which one is higher\n",
        "  and if a specific element is higher then we set that to the max value.\n",
        "  \"\"\"\n",
        "  for i in numList:\n",
        "      if i > max: \n",
        "        max = i\n",
        "  \"\"\"\n",
        "  We compare each element in for loop with min value to see which one is lower\n",
        "  and if a specific element is less then we set that to the min value.\n",
        "  \"\"\"\n",
        "  for j in inputList[::-1]:\n",
        "      if j < min: \n",
        "        min = j\n",
        "\n",
        "  #The range is calculated as the max value minus the min value.\n",
        "  range = max - min\n",
        "\n",
        "  #We output the range.\n",
        "  print(\"The range of the data you entered is:\", range)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "37w_GQEzCfcm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\"\"\"\n",
        "This method will take the sum of all elements in the\n",
        "list and divide it by the count of the elements numbers in the \n",
        "list in order to get the mean or the average. \n",
        "\"\"\"\n",
        "def meanList(numList):\n",
        "  #variable used as a sum variable which we will use to store the sum of each element.\n",
        "  sum = 0\n",
        "  #We take each element in the user entered list and add it up to find the sum of all elements.\n",
        "  for i in numList:\n",
        "    sum += i\n",
        "\n",
        "  #We divide the total sum by the length or count of the the user entered list to get the mean.\n",
        "  mean = sum/len(numList)\n",
        "\n",
        "  #We output the result of the mean or the average.\n",
        "  print(\"The mean of the data you entered is:\", mean)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "R7lU3FgcChhY",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\"\"\"\n",
        "This method is used to retrieve the standard devation of all items in the user entered list.\n",
        "The formula for the standard deviation is : Square root of(sum of (each elment in list - mean of list)^2 / count or length of the list)\n",
        "\"\"\"\n",
        "def numStdDeviation(numList):\n",
        "  sum = 0\n",
        "  sumstddev = 0\n",
        "  stddev = 0\n",
        "  #for loop used to find the sum to retrieve the mean.\n",
        "  for i in numList:\n",
        "      sum += i\n",
        "\n",
        "  #the length of the user entered list would be divided by sum to retrieve the mean\n",
        "  mean = sum/len(numList)\n",
        "\n",
        "  #this foor loop is used to find the sum of (each element in the list and subtract it by the mean)^2\n",
        "  for i in numList:\n",
        "      sumstddev += ((i - mean)**2)\n",
        "\n",
        "  \"\"\"\n",
        "  The standard deviation is retrieved by dividing the sumstnddevaition retrieved from last \n",
        "  for loop by the count of numList and finding the square root of that value. \n",
        "  \"\"\"\n",
        "  stddev = (sumstddev/len(numList))**(1/2)\n",
        "\n",
        "  #prints the standard devaiation value\n",
        "  print(\"The standard deviation of the data you entered is:\", round(stddev, 2))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vrAqSKMlCjY0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\"\"\"\n",
        "This method is used to retrieve the variance of all items in the user entered list. The formula for the variance is :\n",
        "The square of the standard deviation. We use the same steps we used to retrieve the standard deviation in the previous \n",
        "numStdDeviation method and we retrieve the square of that. \n",
        "\"\"\"\n",
        "def numVariance(numList):\n",
        "\n",
        "  sum = 0\n",
        "  sumstddev = 0\n",
        "  stddev = 0 \n",
        "  variance = 0\n",
        "    \n",
        "  #for loop used to find the sum to retrieve the mean.\n",
        "  for i in numList:\n",
        "      sum += i\n",
        "\n",
        "  #the mean is the retrieved sum of the elements in the list divided by the length or count of the elements in the list.\n",
        "  mean = sum/len(numList)\n",
        "\n",
        "  #this foor loop is used to find the sum of (each element in the list and subtract it by the mean)^2\n",
        "  for i in numList:\n",
        "      sumstddev += ((i - mean)**2)\n",
        "\n",
        "  \"\"\"\n",
        "  The standard deviation is retrieved by dividing the sumstnddevaition retrieved from last \n",
        "  for loop by the count of numList and finding the square root of that value. \n",
        "  \"\"\" \n",
        "  stddev = (sumstddev/len(numList))**(1/2)\n",
        "\n",
        "  #The variance will be retrieved by calculating the square of the standard deviation or to the power of 2.\n",
        "  variance = stddev**2\n",
        "\n",
        "  #We print the variance and round it to the closes two decimal places.\n",
        "  print(\"The variance of the data you entered is:\", round(variance, 2))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "orjqFscXClBv",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 119
        },
        "outputId": "c1e85ee5-afa5-4e39-f56a-31d231361d51"
      },
      "source": [
        "#Calls the maxNumber method to see the maximum values entered by the user.\n",
        "maxNumber(inputList)\n",
        "#Calls the minNumber method to see the minimum values entered by the user.\n",
        "minNumber(inputList)\n",
        "#Calls the rangeList method to see the range of the values entered by the user.\n",
        "rangeList(inputList)\n",
        "#Calls the meanList method to see the mean of the values entered by the user.\n",
        "meanList(inputList)\n",
        "#Calls the numStdDeviation method to see the standard deviation of the values entered by the user.\n",
        "numStdDeviation(inputList)\n",
        "#Calls the numVariance method to see the variance of the values entered by the user.\n",
        "numVariance(inputList)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "The maximum number that you entered was: 5432\n",
            "The minimum number that you entered was: 12\n",
            "The range of the data you entered is: 5420\n",
            "The mean of the data you entered is: 675.1\n",
            "The standard deviation of the data you entered is: 1597.26\n",
            "The variance of the data you entered is: 2551250.49\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}