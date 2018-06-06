def tokenize(string, delimiters):
    """ returns token generator 

        :param string: string to tokenize
        :param delimiters: a list of delimiters [ ' ', ',' ]

    """

    accumulator = []
    for char in string:
            if char in delimiters and len(accumulator) > 0:            
                    yield ''.join(accumulator)
                    accumulator = []
            elif char not in delimiters:
                    accumulator.append(char)
    yield ''.join(accumulator)


def stdin():
    """ returns a line generator 
    
    This function is intended to mimic (poorly) the behavior of sys.stdin
    """
    try:
        for line in iter(raw_input, None):
            yield line
    except EOFError:
            pass
                