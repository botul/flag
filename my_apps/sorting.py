content_list = [[125,211,305],[434,584,6],[234,123,756]]

def myFunc(e):
    return e[1]
content_list.sort(reverse=True,key=myFunc)
print (content_list)

