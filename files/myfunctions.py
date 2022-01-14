def media(x):
    '''
    Una funzione per calcolare la media di un array

    Parameters
    ----------
    x : array (numbers)
        un array di numeri

    Returns
    -------
    m : float
        la media dell'array
    '''
    m = 0
    for i in x:
        m += i # += incrementa la variabile somma di i
    m /= len(x) # /= divide la variabile m per len(x)
    return m

def func(x):
    '''
    Una funzione per calcolare il quadrato di un numero

    Parameters
    ----------
    x : number
        un numero

    Returns
    -------
    y : float
        il quadrato del numero
    '''
    y = x*x
    return y
