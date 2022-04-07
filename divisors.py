
def total_divisors(number,*args):
    '''
    Calculates the total number of divisors of number from list of numbers (args)
    '''
    if isinstance(args[0],list):
        number_divisors = sum([1 for i in args[0] if number % i ==0])
        return number_divisors
    elif isinstance(args[0],tuple):
        return total_divisors(number, list(args[0]))
    else:
        number_divisors = sum([1 for i in args if number % i ==0])
        return number_divisors




def divisors(number, **kwargs):
    '''
    Returns bool if there exists any divisors in number list or calculates the total number of divisors of number from list of numbers (args)
    '''
    if kwargs.get('return_bool', -1) == -1 :
        raise ValueError('You must specify return_bool as boolean variable')
    elif len(kwargs) > 2:
        raise ValueError('Only valid arguements are : return_bool, numbers(list/tuple/ndarray)')
    elif not kwargs['return_bool']:
        if isinstance(kwargs['numbers'], list):
            return total_divisors(number, kwargs['numbers'])
        elif isinstance(kwargs['numbers'], tuple):
            return divisors(number, return_bool = False, numbers = list(kwargs['numbers']))
        elif isinstance(kwargs['numbers'], np.ndarray):
            return divisors(number, return_bool = False, numbers = kwargs['numbers'].tolist())
        else:
            raise ValueError('numbers must be list or tuple or ndarray')
    else:
        if isinstance(kwargs['numbers'], list):
            if total_divisors(number, kwargs['numbers']) > 0:
                return True
            return False
        elif isinstance(kwargs['numbers'], tuple):
            return divisors(number,return_bool = True, numbers = list(kwargs['numbers']))
        elif isinstance(kwargs['numbers'], np.ndarray):
            return divisors(number, return_bool = True, numbers = kwargs['numbers'].tolist())
        else:
            raise ValueError('numbers must be list or tuple or ndarray')