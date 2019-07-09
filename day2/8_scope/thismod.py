var = 99

def local():
    var = 0

def glob1():
    global var
    var += 1

def glob2():
    var = 0
    import thismod        # 자기자신을 임포트
    thismod.var += 1      # 전역변수는 그 모듈의 속성이다.

def glob3():
    var = 0
    import sys
    glob = sys.modules['thismod']
    glob.var += 1

def test():
	print(var)
	local()
	glob1()
	glob2()
	glob3()
	print(var)