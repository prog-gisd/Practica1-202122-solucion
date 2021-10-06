RATE = 44471.78

def euros_a_bitcoins(euros):
  return round(euros / RATE, 2)

def bitcoins_a_euros(bitcoins):
  return bitcoins * RATE

def contar_vocales(texto):
  contador = 0
  for letra in texto:
    if letra.lower() in "aeiouáéíóú":
      contador += 1
  return contador

def es_palindromo(text):
  text = str.lower(text).replace(" ", "")
  return text == ''.join(reversed(text))

def max_temperaturas(temperaturas, umbral):
  max_temps = []
  for temp in temperaturas:
    if temp > umbral:
      max_temps.append(temp)
  return max_temps

def cifrar(texto, desplazamiento):
  '''Transforma un texto dado usando cifrado César con un desplazamiento dado.'''
  texto = texto.upper()
  CODE = 'ABCDEFGHIJKLMÑOPQRSTUVWXYZÁÉÍÓÚ'
  cifrado = ""
  for c in texto:
      if c in CODE:
          c = CODE[(CODE.index(c) + desplazamiento) % len(CODE)]
      cifrado += c
  return cifrado


def descifrar(cifrado, desplazamiento):
  '''
  Aplicada a un texto cifrado con el mismo desplazamiento,
  devuelve el texto original.
  '''
  return cifrar(cifrado, -desplazamiento)


mis_productos = []

def insertar(producto):
  mis_productos.append(producto)

def borrar(numero):
  del mis_productos[numero]

def lista_productos():
  return mis_productos

def productos():
  if not mis_productos:
    print('No hay productos')
    return
  for ix, producto in enumerate(mis_productos):
    print(f'{ix}: {producto}')

def cantidad():
  return len(mis_productos)


def menu():
    print('Menú interactivo')
    print()
    while True:
      tokens = input('-> ').split(" ", 1)
      accion = tokens[0]
      if accion == 'convertir':
        src, dst, qty = tokens[1].split()
        if src == 'euros' and dst == 'bitcoins':
          res = euros_a_bitcoins(float(qty))
        elif src == 'bitcoins' and dst == 'euros':
          res = bitcoins_a_euros(float(qty))
        else:
          res = 'Monedas no reconocidas'
        print(res)
      elif accion == 'palindromo':
          palindromo = es_palindromo(tokens[1])
          print(palindromo)
      elif accion == 'contar':
          cuenta = contar_vocales(tokens[1])
          print(cuenta)
      elif accion == 'temperaturas':
        tokens = tokens[1].split()
        temperaturas = tokens[0]
        umbral = tokens[1]
        print(max_temperaturas(temperaturas, umbral))
      elif accion == 'productos':
          if len(tokens) < 2:
            productos()
            continue
          tokens = tokens[1].split()
          sub = tokens[0]
          if sub == 'nuevo':
            insertar(tokens[1])
          elif sub == 'borrar':
            borrar(int(tokens[1]))
      elif accion == 'salir':
        return
      else:
        print("acción no reconocida")

if __name__ == '__main__':
    hm = cifrar('hola mundo', 10)
    print(hm, descifrar(hm, 10), 10)
    hm = cifrar('hola mundo', 15)
    print(hm, descifrar(hm, 15), 15)
    hm = cifrar('adiós, mundo!', 20)
    print(hm, descifrar(hm, 20), 20)
    menu()
