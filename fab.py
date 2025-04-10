
# se trata de rellenar estas dos estructras
#y después pintarlas para que salgan como el pdf
#equipos={1:'Cádiz CB Gades', 2:'Mergablo Conil'}
#periodos={1:{1:2,2:15},2:{1:11,2:3},3:{1:4,2:12},
#     4:{1:19,2:0},5:{1:10,2:4},6:{1:10,2:4}}
def tanper(f):
    periodos={}
    equipos={}
    for linea in f:
        #crear equipos y crear periodos
        lili=linea.split(',')
        evento=lili[0]
        if evento=='eq':
            idEq=int(lili[1])
            nomEq=lili[2]
            equipos[idEq]=nomEq.strip()
        if evento[0]=='Q':
            idcuar=int(evento[1])
            tparcial={}
            for equipo in equipos:
                tparcial[equipo]=0
            periodos[idcuar]=tparcial
        if evento=='b': 
            idEq=int(lili[1].split('#')[0])
            puntos=int(lili[2])
            if periodos[idcuar][idEq]==0:
                periodos[idcuar][idEq]=puntos
            else:
                periodos[idcuar][idEq]+=puntos         
    return periodos, equipos
