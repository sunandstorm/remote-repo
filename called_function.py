def add_two_numbers(a,b):
    return a+b 

def print_list(list1):
    while(len(list1)):
        i=list1.pop()
        print(i)

def make_pizza(*topping):
    """打印顾客点的配料"""
    print(topping)

def print_everything_i_know(
        first,last,
        **information):
    all_info={}
    all_info['first_name']=first
    all_info['last_name']=last

    for key,value in information.items():
        all_info[key]=value
    return all_info