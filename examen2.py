class Permiso():
    def __init__(self):
        self.codigo = []
        self.conductor = []
        self.modelo = []
        self.marca = []
        self.placa = []
        self.ciudad = []
        self.dia = []
        self.mes = []
        self.year = []
        self.motivo = []
        self.habilitado = []
        self.estado = []

    def menu(self):
        opcion = """
            ********** Gestión de Permisos Vehiculares **********
            
                1. Registrar Permiso
                2. Mostrar Todos los Permisos
                3. Habilitar Permisos Habilitados hasta el 31/05/2020
                4. Deshabilitar Permisos
                5. Mostrar Permisos Habilitados
                6. Mostrar Permisos Deshabilitados
                7. Salir
    
            ******************************************************
        """
        print(opcion)
        eleccion = int(input("Seleccione una Opcion del Menú: \n"))
        if(eleccion == 1):
            print(self.registro())
            self.menu()
        elif(eleccion == 2):
            print(self.mostrarPermisos())
            self.menu()
        elif (eleccion == 3):
            print(self.permisosDis())
            self.menu()
        elif (eleccion == 4):
            print(self.permisosNodisponibles())
            self.menu()
        elif (eleccion == 5):
            print(self.perHab())
            self.menu()
        elif (eleccion == 6):
            print(self.perDes())
            self.menu()
        else:
            print("Gracias Por Utilizar el Gestor de Permisos Vehiculares")

    def registro(self):
        codigo = int(input("Digite el codigo: \n"))
        conductor = input("Digite el Nombre del conductor: \n")
        modelo = input("Digite el Modelo del Vehiculo: \n")
        marca =  input("Digite la Marca del Vehiculo: \n")
        placa = input("Digite la Placa del Vehiculo: \n")
        ciudad = input("Digite la Ciudad: \n")
        dia= input("dia del mes: \n")
        mes = input("mes: \n")
        year = input("an-o: \n")
        motivo = input("Motivo de la Solicitud: \n")
        print(self.guardar(codigo, conductor, modelo, marca, placa, ciudad, dia, mes, year, motivo))
        registrOtro = input("Desea Registrar Otro Permiso? S/N")
        if(registrOtro == "s" or registrOtro == "S"):
            self.registro()
        else:
            return "Permiso Agregado correctamente."

    def guardar(self, codigo, conductor, modelo, marca, placa, ciudad, dia, mes, year, motivo):
        self.codigo.append(codigo)
        self.conductor.append(conductor)
        self.modelo.append(modelo)
        self.marca.append(marca)
        self.placa.append(placa)
        self.ciudad.append(ciudad)
        self.dia.append(dia)
        self.mes.append(mes)
        self.year.append(year)
        self.motivo.append(motivo)
        self.habilitado.append(0)
        self.estado.append(1)
        return "El Permiso del conductor {} se ha regitrado correctamente.".format(conductor)

    def mostrarPermisos(self):
        if(self.conductor):
            for i in range(len(self.conductor)):
                self.informacion(i)
            return "Estos son todos los permisos."
        else:
            return "No hay ningun permiso para mostrar."

    def informacion(self, posicion):
        if(self.estado[posicion] == 1):
            print("********** Conductor: {} **********".format(self.conductor[posicion]))
            print("Codigo: {} ".format(self.codigo[posicion]))
            print("Modelo: {} ".format(self.modelo[posicion]))
            print("Marca: {} ".format(self.marca[posicion]))
            print("Placa: {} ".format(self.placa[posicion]))
            print("Ciudad: {} ".format(self.ciudad[posicion]))
            print("Fecha de Solicitud: {}/ {} /{}".format(self.dia[posicion],self.mes[posicion],self.year[posicion]))
            print("Motivo: {} ".format(self.motivo[posicion]))
            if(self.habilitado[posicion] == 1):
                print("Habilitado: Sí")
            elif(self.habilitado[posicion] == 0):
                print("Habilitado: No")
            pass

    def permisosDis(self):
        if self.conductor:
            self.mostrarPermisos()
            validar = input(" Digite el conductor del permiso que desea Habilitar: \n")
            posicion = self.conductor.index(validar)
            if(self.dia[posicion] <= 31 and self.mes[posicion] <= 5 and self.year[posicion] <= 2020):
                print(self.habilitarPer(posicion))
            else:
                return "No Hay nada.."

    def habilitarPer(self, cosa):
        self.habilitado[cosa] = 1
        return "Habilitado exitosamente...."

    def permisosNodisponibles(self):
        if self.conductor:
            self.mostrarPermisos()
            validar = input(" Digite el conductor del Permiso que desea deshabilitar: \n")
            cosa2 = self.conductor.index(validar)
            print(self.desPermiso(cosa2))
        else:
            return "No hay nada...."

    def desPermiso(self, cosa2):
        self.habilitado[cosa2] = 0
        return "Deshabilitado exitosamente...."

    def perHab(self):
        # self.informacion()
        mostrar = False
        for i in range(len(self.conductor)):
            if(self.habilitado[i] == 1):
                self.informacion(i)
                mostrar = True
        if(mostrar == False):
            return "No hay ningun Permiso Aqui."

    def perDes(self):
        # self.informacion()
        mostrar = False
        for i in range(len(self.conductor)):
            if(self.habilitado[i] == 0):
                self.informacion(i)
                mostrar = True
        if(mostrar == False):
            return "No hay ningun Permiso Aqui."

    # def habPorFe(self):
    #     fecha1 = "31/5/2020"
    #     if(self.fecha_solicitud <= fecha1):
    #         self.informacion(i)
    #         print("Los permisos en la fecha correspondiente")
    #     else:
    #         return "No hay ningun Permiso Disponible"
    #     pass


permisos = Permiso()
permisos.guardar("1", 'jose mercado', 'corolla', 'toyota', '2504tda', 'santa cruz', 1,6,2020, 'permiso para ir al trabajo')
permisos.guardar(2, 'alberto mercado', 'hilux', 'toyota', '2640sda', 'tarija' ,12,4,2020, 'permiso para ir al trabajo')
permisos.guardar(3,'gabriel melgar', 'sentra', 'nissan', '3204nts', 'beni' ,30,5,2020, 'permiso para ir al trabajo')
permisos.guardar(4, 'carla medina', 'lancer', 'mitsubishi', '2207sba', 'chuquisaca' ,2,5,2020, 'permiso para ir al trabajo')
permisos.guardar(5, 'pablo aguilar', 'accord', 'honda', '3504atd', 'cochabamba' ,9,4,2020, 'permiso para ir al trabajo')
permisos.guardar(6, 'carlos montero', 'civic', 'honda', '2804sta', 'santa cruz' ,10,6,2020, 'permiso para ir al trabajo')
permisos.guardar("7", 'pablo aleman', 'yaris', 'toyota', '2054pda', 'la paz' ,22,6,2020, 'permiso para ir al trabajo')
permisos.menu()