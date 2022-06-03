print('welcome to Chedraui🥵😩🦵')
name=input('name:')

p1=input('product:')
c1=int(input('cost:'))

p2=input('product:')
c2=int(input('cost:'))

p3=input('product:')
c3=int(input('cost:'))

p4=input('product:')
c4=int(input('cost:'))

p5=input('product:')
c5=int(input('cost:'))

semitotal=c1+c2+c3+c4+c5
iva= semitotal*0.16
total= semitotal+iva

print(name,'this is your ticket:')
print(p1,'$',c1)
print(p2,'$',c2)
print(p3,'$',c3)
print(p4,'$',c4)
print(p5,'$',c5)
print('IVA:',iva)
print('subtotal:',semitotal)
print('total:', total)