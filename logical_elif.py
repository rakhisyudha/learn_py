input_temp = input('How many temperature today?: ')
temp = int(input_temp)
if temp > 30:
    print('its a hot day')
elif temp < 10:
    print('its a cold day')
else:
    print('its a normal day')