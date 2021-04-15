st = 'Programming'
#자음이 나타나는 동안만 출력하는 기능
for ch in st:
    if ch not in ['a', 'e', 'i', 'o', 'u']:
        continue #모음이 아닌 경우 반복문을 건너뛴다.
    print(ch)
print('The end')