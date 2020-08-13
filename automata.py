import json

gramatica = {}

with open('D:\Programming\Python\LanguagesStructure\gramatica.JSON', 'r', encoding='utf8') as f:
    archivo_json = f.read()
    gramatica = json.loads(archivo_json)

no_terminales = gramatica.keys()
terminales = gramatica.values()

class Estado:
    gramatica = {}

    def __init__(self, numero, siguiente = None):
        self.numero = numero
        self.siguiente = siguiente

class Automata:
    #estados = {i0: [(E, i1), ...]}
    grafo = {}
    estados = []

    def __init__(self):
        i0 = Estado(0)
        i0.gramatica = gramatica
        self.estados.append(i0)

    def solucionar(self, estado, i=0):
        for nt, producciones in estado.gramatica.items():
            #print(nt)
            for produccion in producciones:
                transicion = self.evaluar_punto(produccion, i)
                nuevo_estado = self.crear_nuevo_estado(producciones, transicion, i+1)
                self.estados[i].siguiente = self.estados[i+1]


                self.estados.append(nuevo_estado)
                #crear_nuevo_estado(...)
                #solucionar(nuevo_estado, i+1)
                

    def mover_punto(self, produccion):
        i = produccion.index('.')
        produccion.insert(i+2,'.')
        produccion.remove('.')        
        print(produccion)
        return produccion

    def evaluar_punto(self, produccion, i):
        i = produccion.index('.')
        if i == len(produccion)-1:
            return None
        elif produccion[i+1] in no_terminales:
            if i != 0:
                self.estados[i].gramatica.update({produccion[i+1]: self.obtener_producciones(produccion[i+1])})
            return produccion[i+1]
        else:
            return produccion[i+1]

    def obtener_producciones(self, no_terminal):
        return gramatica[no_terminal]

    def crear_nuevo_estado(self, producciones, transicion, i):
        nueva_gramatica = {}
        for produccion in producciones:
            i = produccion.index('.')
            if i == len(produccion)-1:
                return None
            elif produccion[i+1] == transicion:
                nueva_produccion = self.mover_punto(produccion)
                no_terminal = self.obtener_noterminal(produccion)
                nueva_gramatica.update({no_terminal, nueva_produccion})

        nuevo_estado = Estado(i+1)
        nuevo_estado.gramatica = nueva_gramatica
        return nuevo_estado

    def obtener_noterminal(self, produccion):
        for nt, producciones in gramatica.items():
            for prod in producciones:
                copia_produccion = produccion
                copia_produccion_inicial = prod

                copia_produccion.remove('.')
                copia_produccion_inicial.remove('.')

                if copia_produccion == copia_produccion_inicial:
                    return nt

automata = Automata()
automata.solucionar(automata.estados[0])
        

