def sum_positive_numbers( ListOfNumbers ):
    Total = 0
    for number in ListOfNumbers:
        if number > 0:
            Total += number
    return Total

ListOfNumbers = [5,7,-8,0,8,9,-55,5,10,-1,1]
print(sum_positive_numbers(ListOfNumbers))