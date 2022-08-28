#!/bin/env python3.9
import copy

def ret_perm(lst,tmp_lst,ret_lst):
    if not lst:
        ret_lst.append(tmp_lst)
        return
    for item in lst:
        tmp_lst_send = copy.deepcopy(tmp_lst)
        tmp_lst_send.append(item)
        lst_send = copy.deepcopy(lst)
        lst_send.remove(item)
        ret_perm(lst_send,tmp_lst_send,ret_lst)

def main():
    numbers = ["2","3","5","8"]
    operations = ["+","-","*","/"]
    order = [0,1,2]
    permutations = []
    ord_perm = []
    # I chose to implement the permutations instead to use import itertools.permutation
    ret_perm(numbers,[],permutations)
    ret_perm(order,[],ord_perm)
    d = {}
    for lst in permutations:
        # for each operation there are 4 options
        for op1 in operations:
            for op2 in operations:
                for op3 in operations:
                    eval_lst = [lst[0],op1,lst[1],op2,lst[2],op3,lst[3]]
                    #there is order of execution
                    for ord_op in ord_perm:
                        ord_op_orig= copy.deepcopy(ord_op)
                        eval_lst_copy = copy.deepcopy(eval_lst)
                        for i in range(3):
                            # try beacuse there is division by zero
                            try:
                                num_of_op=ord_op[i]
                                res= eval(f"{eval_lst_copy[num_of_op*2]}{eval_lst_copy[num_of_op*2+1]}{eval_lst_copy[num_of_op*2+2]}")
                                eval_lst_copy.insert(num_of_op*2+3,res)
                                del eval_lst_copy[num_of_op*2:num_of_op*2+3]
                                if i==0 and ord_op[1] > ord_op[0]:
                                    ord_op[1] -= 1
                                if (i==0 and ord_op[2] > ord_op[0])or(i==1 and ord_op[2] > ord_op[1]):
                                    ord_op[2] -= 1
                            except:
                                # division by zero
                                res = 999
                                break
                        if res in d.keys():
                            d[res][0] +=1
                        else:
                            d[res] = [1]
                        # save all the ways to get this key
                        d[res].append([lst,op1,op2,op3,ord_op_orig])
    # filter not native 
    d_int = {int(k):d[k] for k in d.keys() if (float(k) - int(k)) == 0 and k>=0 and k!=999}
    for k in sorted(d_int.keys()):
        print(k,": ",d[k][0])
    


if __name__ == "__main__":
    main()
