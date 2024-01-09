class A():
    def __init__(self, a) -> None:
        self.a = a 

    def __repr__(self) -> str:
        return f'A({self.a})'
    
    def modif(self, a):
        self.a = a
    
class B(A):
    def __init__(self, b) -> None:
        self.b = b 

    def __repr__(self) -> str:
        return f'{self.a} {self.b}'
    
def jesuisunefonction(a):
    a = 2
    return A(a)

print(jesuisunefonction(1).a)

o = B(1)
o.modif(2)
print(o)