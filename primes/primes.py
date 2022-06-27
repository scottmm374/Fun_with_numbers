import math


def main():

    cols, num_range = input(int("Cols, Range: ")).split()



#*<----------------------------------------------------------------------------->
def calc_rows(cols:int, num_range:int):

    num_rows = math.ceil(num_range/cols)

    return(num_rows, cols, num_range)

#*<----------------------------------------------------------------------------->
def generate_primes(n: int) -> list:
    """
        Generates a list of Prime numbers, equal to n(max range of numbers)
        n: integer of max range of prime list
        returns: a list of Prime intergers
    """

    prime_list = list()

    # outer loop for full range of numbers up to N
    for num in range(0,n):
        if num > 1:
            # Inner loop range checks range of 2, to current num from outer loop. Checks if there are any divisors, if % not 0 its Prime 
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    prime_list.append(num)
    return prime_list


#*<----------------------------------------------------------------------------->
def create_integer_matrix(cols:int, rows:int) -> list:
    """
     Creating an empty matrix equal to column widths filled with zeros to save space
     cols: interger - Number of columns 
     rows: integer - calculated rows needed for range
     return : List, Matrix filled with sequential numbers
     """
    matrix = [[0] * cols for x in range(1,rows)]

    num = 0
    for y in range(len(matrix)):
            for x in range(cols):
                num +=1
                matrix[y][x] = num
    return matrix

#*<----------------------------------------------------------------------------->
def remove_non_primes(arr:list, primes:list, cols:int) -> list:
    # Checks array with sequential numbers against primes list
    for row in range(len(arr)):
            for col in range(cols):
                # If not prime, replace number with '*'- For visual purposes
                if arr[row][col] not in primes:          
                        arr[row][col] = ' *'
                # If it is prime, replace with 99 - also for visual purposes
                else:
                    arr[row][col] = '99'
            
    return arr

if __name__=="__main__":
    main()