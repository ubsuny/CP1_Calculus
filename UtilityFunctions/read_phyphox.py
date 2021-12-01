from numpy import genfromtxt

def read_phyphox(file_name = "elevator.txt", verbose=False):
    '''
    # from phyphox app data.
    # Experiment performed in elevator.
    #
    #  Two columns of data: time (s) and acceleration (m/s^2).
    #
    '''

    data = genfromtxt(file_name, comments='#')

    time = data[:,0]
    acceleration = data[:,1]
    if verbose:
        print (time)
        print(acceleration)
    return [time, acceleration]
