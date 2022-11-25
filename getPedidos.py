import oracle_connect

lista = []


""" def novosPedidos():
    consulta = oracle_connect.consultaAberto()
    result = consulta.fetchone()
    if(result):
        aux = []
        numped = result[0]
        cliente = result[13]
        data = str(result[5]).split(' ')[0].split('-')
        datastr = ('%s/%s/%s' % (data[2], data[1], data[0]))
        status = 'a'
        verificacao = psql_connect.verificar(numped)
        if(verificacao):
            pass
        else:
            psql_connect.insert(numped)
            lista = [numped, cliente, datastr, status]
            return(lista)

    else:
        pass
 """


def novosPedidos():
    cursor = oracle_connect.Pedidos()
    result = cursor.fetchone()
    lista = []
    while(result):
        numped = result[0]
        cliente = result[13]
        data = str(result[5]).split(' ')[0].split('-')
        datastr = ('%s/%s/%s' % (data[2], data[1], data[0]))
        sep = result[4]
        conferido = result[10]
        ec= result[9]
    
        if(conferido):
            status = 'c'
        elif(ec):
            status = 'ec'
        elif(sep):
            status = 'sep'
        else:
            status = 'em'
        aux = [numped, cliente, datastr, status]
        lista.append(aux)
        result = cursor.fetchone()
    return(lista)
