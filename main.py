#!/usr/bin/env python

def get_list2d(row,col):
    """ ask user input sizes from 7 college """
    size = {
    0: " Small",
    1: "Medium",
    2: " Large",
    3: "Xlarge"}
    a = [[0 for j in range(col)] for i in range(row)]
    for j in range(col):
        for i in range(row):
            a[i][j] = input("College %d, %s: " % (j+1,size[i]))
        
        for r in a:
            print r
    return a

def row_sum(a,row,col):
    """ allocate list b is initialized to zero
        store row sum in list b
        return b, a list of row sum
    """
    b = [0 for i in range(row)]
    for i in range(row):
        s = 0
        for j in range(col):
            s = s + a[i][j]
        b[i] = s
    return b


def col_sum(a,row,col):
    """ allocate list c is initialized to zero
        store col sum in list c
        return c,a list of col sum
    """
    c = [0 for j in range(col)]
    for j in range(col):
        s = 0
        for i in range(row):
            s = s + a[i][j]
        c[j] = s
    return c

def grand_total(a,row,col):
    """ calculate total of sweetshirts """
    total = 0
    for i in range(row):
        for j in range(col):
            total = total + a[i][j]
    return total

def print_summary():
    """ print header """
    head1 = "Inventory Report"
    head2 = "College"
    print ("%+55s" % str(head1))
    print
    print ("%+50s" % str(head2))
    print 
    print "%25d"%1,"%7d"%2,"%7d"%3,"%7d"%4,"%7d"%5,"%7d"%6,"%7d"%7,"%14s"%("Size Total")

def print_sm(a,b,row,col,size):
    """ print row of size small and medium """
    for i in range(row-2):
        print
        print "\t",size[i],"\t",
        for j in range(col):
            print "\t",a[i][j],
        print "\t",b[i]
    print "%s" % ("Size")
    
def print_lxl(a,b,row,col,size):
    """ print row of size largea and xlarge """
    for i in range(row-2,row):
        print
        print "\t",size[i],"\t",
        for j in range(col):
            print "\t",a[i][j],
        print "\t",b[i]

def print_colsum(a,c,row,col):
    """ print sum of sweetshirts needed from each college """
    print
    print "  College Total", 
    for j in range(col):
        print "\t",c[j],
    print


def print_total(total):
    """ print total inventory of all sweatshirts """
    t = total
    print "\n"
    print ("%60s" % str("Total Quantity On Hand = ") + str(t))
    return t

def main():
    """ main function """
    row = 4
    col = 7
    size = {
    0: " Small",
    1: "Medium",
    2: " Large",
    3: "Xlarge"}
    a = get_list2d(row,col)
    b = row_sum(a,row,col)
    c = col_sum(a,row,col)
    total = grand_total(a,row,col)
    print_summary()
    print_sm(a,b,row,col,size)
    print_lxl(a,b,row,col,size)
    print_colsum(a,c,row,col)
    print_total(total)
if __name__ == "__main__":
    main()
