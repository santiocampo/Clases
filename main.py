import interfaz
import logica

interfaz.imprimirNombre("Santiago")
interfaz.imprimirVariable("Número", [1,2,3])
interfaz.separador("-")

resultado1= logica.sumar3Numeros(2,4,5)
resultado2= logica.sumarNumeros(1,2)
resultado3= logica.sumarListas([1,2,3],[3,2,1])

interfaz.imprimirVariable("Sumar 3 números", resultado1)
interfaz.imprimirVariable("Sumar N números", resultado2)
interfaz.imprimirVariable("Sumar 2 listas", resultado3)
