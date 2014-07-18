def even_func(n):
    """Function defines if divides by exactly two"""
    if n % 2 != 0:
	    return True
    else:
	    return False


def fizz_buzz(n):
    """determines fizz_buzz value"""
    count = 1
    while count <= n:
        if count % 3 == 0 and count % 5 == 0:
                print 'fizz buzz'
                count += 1
        elif count % 3 == 0:
                print 'fizz'
                count += 1
        elif count % 5 == 0:
                print 'buzz'
                count += 1
        else:
                print count
                count += 1

fizz_buzz(100)
