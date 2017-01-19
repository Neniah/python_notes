def addition(num1, num2):
    answer = num1 + num2
    return answer

x = addition(5, 6)
print x

def website(font, background_color, fontsize, font_color):
    print('font:', font)
    print('bg:', background_color)
    print('Font size: ', fontsize)
    print('Font color:', font_color)


website('TNR', 'white', '11', 'black')

website(background_color='white',
        fontsize='11',
        font_color='black',
        font='TNR')
