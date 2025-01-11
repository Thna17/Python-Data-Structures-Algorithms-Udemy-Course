dic1 = {
    'value': 11
}
dic2 = dic1 

print('Before num2 value is updated:')
print('num1 = ', dic1)
print('num2 = ', dic2)

dic2['value'] = 22

print('\nAfter num2 value is updated:')
print('num1 = ', dic1)
print('num2 = ', dic2)

print('\nnum1 point to', id(dic1))
print('num2 point to', id(dic2))