

# def func1():
#     print("aaa")


def func2(func1):
    print("bbb")
    def ddd():
        print("cccc")
        func1()
        print("zzzz")
    return ddd()

@func2
def test():
    print("tst")


test()