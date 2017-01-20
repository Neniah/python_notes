
appendMe = 'Some text'

saveFile = open('exampleFile.txt', 'a')
saveFile.write(appendMe)
saveFile.close()
