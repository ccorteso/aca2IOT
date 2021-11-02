#Trae la data desde un .txt programacion funcional λ
with open("Data.txt") as file:
    for data in file:
        #convierte en arreglo
        dataArray = data.split(";")
        #toma el valor de array lo convierte en int
        sueldo = abs(int(dataArray[2]))
        #informacion de empleado
        informacionPersona = dataArray[:2]
        #inico de horas Extras
        dataInicial = lambda arg,num : arg[num:]
        dataHora =  dataInicial(dataArray,3)
        #busca recibe lista y devuelve la posicion
        finalArray =  lambda args: args.index('-1')
        #pasa todos los valores str a int
        strAInt = lambda arg: list(map(lambda num:int(num) ,arg[:finalArray(arg)]))
        horasExtras = strAInt(dataHora)
        #inicio de los datos de ventas
        dataVentas = dataInicial(dataHora,(finalArray(dataHora)+1))
        ventasRealizadas = strAInt(dataVentas)
        # aplica solo a horas extras diurnas
        valoresDeHoraExtras = list(map(lambda num: round(((sueldo / 30) / 8) * 1.25) * num, horasExtras))
        #analiza si la persona trabajo mas o vende mas
        area = lambda largoHr,largoVen: 'Administrativo' if len(largoHr) > len(largoVen) else "Ventas"

        if area(horasExtras,ventasRealizadas) == 'Administrativo':
           # aplica 50% a la hora extra
           aplicandoIncremento = list(map(lambda sueldo:round(sueldo + (sueldo*0.50)),valoresDeHoraExtras))
           print(f"Area: {area(horasExtras,ventasRealizadas)}, "
                 f"Empleado: {informacionPersona}, sueldo: ${sueldo}, "
                 f"Total a pagar: ${round((sueldo + sum(aplicandoIncremento) - (sueldo + sum(aplicandoIncremento))*0.12))}, "
                 f"Descuentos parafiscales 12%: {round((sueldo + sum(aplicandoIncremento))*0.12)}")
        else:
            # aplica comision de 5%
            aplicandoIncrementoVentas = list(map(lambda ventas:round(ventas * 0.05),ventasRealizadas))
            print(f"Area: {area(horasExtras, ventasRealizadas)}, "
                  f"Empleado: {informacionPersona}, sueldo: ${sueldo}, "
                  f"Total a pagar: ${round((sueldo + sum(aplicandoIncrementoVentas)+sum(valoresDeHoraExtras)) - (sueldo + sum(aplicandoIncrementoVentas) + sum(valoresDeHoraExtras))*0.12)}, "
                  f"Descuentos parafiscales 12%: {round((sueldo + sum(aplicandoIncrementoVentas)) * 0.12)}")






