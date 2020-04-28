print('its alive')

x = 9
y = 'asdf'

x = x.__neg__()
y = y.upper()

print(x)
print(y)

def my_fn():
    print('something')



if x>0:
    my_fn()
elif x==0:
    print(x)
else:
    print(y)


l = list(range(5))
for item in l:
    print(f'item={item}')
