def inner_fn():
    print('i am an inner function')

def wrapper_fn(fn):
    print('i am an wrapper function')

    def updated_fn():
        print('i am updated function')
        fn()
    
    return updated_fn

# updated_fn = wrapper_fn(inner_fn)

# updated_fn()
# updated_fn()

some_list = [1,2,3,4,5,6,7,8,9]
# [2,4,6,8]
# [4,6,12,16]
new_list = []
for item in some_list:
    if item % 2 != 0:
        continue
    new_list.append(item*2)
print(new_list)

# def filter_fn(item):
#     return item % 2 == 0

# def map_fn(item):
#     return item * 2

new_list = list(map(lambda i:i * 2, filter(lambda i:i % 2 == 0, some_list)))
print(new_list)