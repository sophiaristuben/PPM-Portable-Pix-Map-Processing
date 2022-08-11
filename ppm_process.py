"""
    CS051P Lab Assignments: PPM Processing

    Author: Gloria Lee
    Partner: Sophia Ristuben

    Date:   4/14/21

    The goal of this assignment is to give you practice working with nested lists
    by writing a program that manipulates the entire image with multiple lines.
"""


def process(lines, rows, cols):
    """
    Store the body of the image as a nested list

    :param lines: (str) list of strings representing body of image
    :param rows: (int) number of rows
    :param cols: (int) number of cols
    :return: (list) list of inner lists composed of row integers
    """
    
    integerList = []
    
    # add all of the integers into one list 
    for line in lines:
        for num in line.split():
            integerList.append(int(num))
    
    # takes total number of integers and divides by row to find number of integers in each row 
    if rows != 0:
        num_Int_Row = len(integerList) / rows
    else:
        num_Int_Row = 0

    rowList = []
    
    # loops through the number of rows and creates new list each with number of row integers found before
    for row in range(rows):
        rowList.append(integerList[int(row * num_Int_Row): int((row + 1) * num_Int_Row)])

    return rowList

def read_ppm(filename):
    """
    Opens the file with the filename, reads it, calls process with the appropriate rows and cols and returns the list of list from process

    :param filename: (str) file to open
    :return: (list) list of inner list composed of integer
    """

    # open file and read to the second line
    open_file = open(filename, "r", encoding = "latin-1")
    open_file.readline()
    row_col = open_file.readline()

    
    # split second line string into list and define indexes to row and column number
    row_col_list = row_col.split()
    col = int(row_col_list[0])
    row = int(row_col_list[1])
    open_file.readline()

    # making the list of strings for the body to give to the process function
    lines = []
    for line in open_file:
        lines.append(line)

    # return the list of inner lists from process function 
    return process(lines, row, col)

def write_ppm(image, filename):
    """
    The function interprets this list of lists as an image and writes out a valid ppm file to an output file with name filename.

    :param image: (list) lists of lists of integers with values between 0 and 255
    :param filename: (str) ppm file that image is written to
    """

    open_file = open(filename, "w")
    
    # write the header of the file
    open_file.write("P3\n")
    width = int(len(image[0])/3)
    height = len(image)
    open_file.write(str(width) + " " + str(height)+ "\n")
    open_file.write("255\n")

    # write the body of the file
    for row in image:
        line = ""
        for num in row:
            line += str(num) + " "
        line.strip()
        open_file.write(line + "\n")


def scale(image, row_scale, col_scale):
    """
    This function takes an image (list of lists) and scales it according to the scale values and returns the output list of lists

    :param image: (list) list of lists of integers as returned by process
    :param row_scale: (int) scale for rows
    :param col_scale: (int) scale for columns
    :return: (list) of rows and columns with appropriate scale
    """
    
    newList = []
    
    # loops through number of inner lists in image
    for row in range(len(image)):
        rowList = []
        count = 0
        # if the index of the inner list is divisible by row scale
        if row % row_scale == 0:
            for col in range(0, len(image[row]), 3):
                # if the col number mod the col_scale is 0, you add the index of the row from the col to the next 3 
                if count % col_scale == 0:
                    rowList.extend(image[row][col:col+3])
                count += 1
            # append the rowList to the newList being created
            newList.append(rowList)

    return newList


def main():
    """
    Ask user for the filenames, the scales (which must be valid), and change the output file accordingly
    """
    # asks user for input and output file names
    input_file = input("Enter input file: ")
    output_file = input("Enter output file: ")
    
    # while height and width not positive integers keeps asking 
    height = input("Enter height scaling factor: ")
    while not height.isdigit() or int(height) <= 0: 
        height = input("Enter height scaling factor: ")
    
    width = input("Enter width scaling factor: ")
    while not width.isdigit() or int(width) <= 0:
        width = input("Enter width scaling factor: ")

    # reads input file and then scales with appropriate scaling factors then writes scaled filed into output file
    write_ppm(scale(read_ppm(input_file), int(height), int(width)), output_file)



if __name__ == '__main__':
    main()