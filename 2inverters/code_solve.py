#!/bin/env python3.9
import copy
def print_created(st,lst,depth):
    for item in lst:
        if item[0] == st:
                print(depth*" " + str(item))
                if item[1][0] == "in":
                    return
                if item[1][1] == "or" or item[1][1] == "and":
                    print_created(item[1][0],lst, depth+1)
                    print_created(item[1][2],lst, depth+1)
                if item[1][0] == "not":
                    print_created(item[1][1],lst, depth+1)
                

def check_for_solving(lst):
    abc_inverted = [{0,1,2,3},{0,1,4,5},{0,2,4,6}]
    for inverted in abc_inverted:
        exist = False
        for item in lst:
            if item[0] == inverted:
                exist = True
        if not exist:
            return False
    print("\nsolved!!!\n*****************")
    for inverted in abc_inverted:
        for item in lst:
            if item[0] == inverted:
                print_created(inverted,lst,0)
                print(f"*****************")
    
def not_in_expr_lst(func,lst):
    for item in lst:
        if item[0] == func:
            return False
    return True

def expand_expr(lst,idx):
    while idx < len(lst):
        for i in range(idx):
            and_op = lst[i][0].intersection(lst[idx][0])
            and_op_created = [lst[i][0],"and",lst[idx][0]]
            if not_in_expr_lst(and_op, lst):
                lst.append([and_op,and_op_created])

            or_op = lst[i][0].union(lst[idx][0])
            or_op_created = [lst[i][0],"or",lst[idx][0]]
            if not_in_expr_lst(or_op, lst):
                lst.append([or_op,or_op_created])
        idx+=1

def main():
    #create list of a,b,c
    expr = [[{4,5,6,7},"in"],[{2,3,6,7},"in"],[{1,3,5,7},"in"]]
    #exapnd the list for all the possible combination using OR and AND gates
    expand_expr(expr,1)

    print("The initial functions:")
    for item in expr:
        print(item[0])

    set_of_all = {i for i in range(8)}
    expr_deepcopy = copy.deepcopy(expr)

    
    for i in range(len(expr)):
        expr = copy.deepcopy(expr_deepcopy)
        #create not on all the possible function
        expr.append([set_of_all.difference(expr[i][0]),["not",expr[i][0]]])
        #exapnd all the possible options
        expand_expr(expr,len(expr)-1)
        one_not_expr_deepcopy = copy.deepcopy(expr)
        for j in range(len(expr)):
            expr = copy.deepcopy(one_not_expr_deepcopy)
            #create the second not on all the possible options
            expr.append([set_of_all.difference(expr[j][0]),["not",expr[j][0]]])
            #expand to all the possible options
            expand_expr(expr,len(expr)-1)
            check_for_solving(expr)


if __name__ == "__main__":
    main()
