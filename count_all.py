def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    p=txt
    m=0
    x1=0
    n=len(p)
    for i in p:
        if (i.isalpha()):
            m=m+1
            x1=n-m
    return m , x1
print(count_all("1Salom323") )
