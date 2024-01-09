"""Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función."""


def areacirculo (x):
    pi = 3.1415
    return pi*x**2
print (areacirculo(4))

def areacilindro (x, altura):
    return areacirculo(x)*altura

print (areacilindro(4,10))
    
