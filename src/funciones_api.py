def web_atleta (lista_id):
    '''
    Esta función recorre una lista de id de atletas, para luego generar las url de cada atleta.
    '''
    url_lista = []
    for n in lista_id:
        n = str(n)
        url_tri = "https://api.triathlon.org/v1/athletes/"
        url = url_tri + n
        url_lista.append(url)
    return url_lista