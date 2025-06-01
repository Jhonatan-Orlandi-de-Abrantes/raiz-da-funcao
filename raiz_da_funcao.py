a = int(input('1º valor: '))
b = int(input('2º valor: '))
c = int(input('3º valor: '))

Delta = b**2 - 4*a*c

if Delta < 0:
    print('Não existe raiz.')
elif Delta == 0:
    print(Delta)
    raiz = -b / (2*a)
    print(f'Raíz: S=({raiz:.1f})')
else:
    if b == 0:
        bhksoma = (Delta**0.5) / (2*a)
        print(f'Delta = {Delta:.1f}')
        print(f'Bhaskara = {Delta**0.5:.1f} / {2*a}')
        print(f'Raíz: S=({bhksoma:.1f})')
    else:
        bhksoma = (-b + Delta**0.5) / (2*a)
        bhksub = (-b - Delta**0.5) / (2*a)

        print(f'Delta = {Delta:.1f}')
        print(f'Bhaskara = {-b} +- {Delta**0.5:.1f} / {2*a}')
        print(f'Raízes: S=({bhksoma:.1f}, {bhksub:.1f})')