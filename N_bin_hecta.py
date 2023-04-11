#funcion que converte un numero a binario y a hexadecimal, reto de la semana alv


num = int(input('Ingresa el número que deseas convertir:'))

def decimal_a_binario(decimal):
    """Convierte un número decimal a su representación binaria."""
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    return binario

num2 = decimal_a_binario(num)
print('El número binario sería: '+ num2)