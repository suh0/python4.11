pos = [0] * 8
flag = [False] * 8

def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()
    
def set(i: int) -> None:
    for k in range(8):
        if not flag[k]:
            pos[i] = k
            if i == 7:
                put()
            else:
                flag[k] = True
                set(i + 1)
                flag[k] = False
            
set(0)