import threading

def f():
    print('thread function')
    return

if __name__ =='__main__':
# To know more about that:
# '''https://stackoverflow.com/questions/419163/what-does-if-name-main-do'''
    for i in range(3):
        t = threading.Thread(target=f)
        t.start()
