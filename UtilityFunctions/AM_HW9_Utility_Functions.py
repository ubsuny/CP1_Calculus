def total_distance(filename,est):
    """
    Calculates the total distance and efficiency of a trip given some `PhyPhox` csv file.
    
    Inputs:
    filename - Name of the csv file. Include the .csv extension. (str)
    est - The estimated net displacement from starting to ending location. (float)
    
    Returns:
    Returns the percentage efficiency of your trip given to the hundredths place. (float)
    
    """
    data = pd.read_csv(filename)
    a_x = data["Linear Acceleration x (m/s^2)"].to_numpy()
    a_y = data["Linear Acceleration y (m/s^2)"].to_numpy()
    a_z = data["Linear Acceleration z (m/s^2)"].to_numpy()
    t = data["Time (s)"]
    t = t.to_numpy()
    v_x = integrate.simps(a_x,t)
    v_y = integrate.simps(a_y,t)
    v_z = integrate.simps(a_z,t)
    d_x = v_x*(t[-1]-t[0])
    d_y = v_y*(t[-1]-t[0])
    d_z = v_z*(t[-1]-t[0])
    d_tot = sqrt(d_x**2 + d_y**2 + d_z**2)
    d_mi = d_tot / 1609
    eff = est*100 / d_mi
    print("You travelled to total distance of {} miles.".format(round(d_mi,2)))
    print("You estimated your total travel to be {} miles, which means your driving was {}% straight to your destination."
          .format(est,round(eff,2)))
    return(round(eff,2))

def coast_time(filename):
    """
    Calculates the length of minimal acceleration or coasting and the percentage of the trip that involved coasting.
    
    Inputs: 
    filename - Name of the csv file. Include the .csv extension. (str)
    
    Returns:
    Returns the percentage that you coasted on your trip to the hundredths place. (float)
    
    """
    data = pd.read_csv(filename)
    a_x = data["Linear Acceleration x (m/s^2)"].to_numpy()
    a_y = data["Linear Acceleration y (m/s^2)"].to_numpy()
    a_z = data["Linear Acceleration z (m/s^2)"].to_numpy()
    t = data["Time (s)"]
    a_x_2 = a_x.tolist()
    a_y_2 = a_y.tolist()
    a_z_2 = a_z.tolist()
    t_2 = t.to_numpy()
    points = 0
    for entry in range(0,len(a_x_2)):
        if (-0.10 < a_x_2[entry] < 0.10) and (-0.10 < a_y_2[entry] < 0.10) and (-0.10 < a_z_2[entry] < 0.10) :
            points = points + 1
    time_per_point = (t_2[-1] - t_2[0]) / len(t)
    coast_time = points * time_per_point / 60
    coast_eff = coast_time / (t_2[-1] - t_2[0]) * 6000
    coast_time = round(coast_time,2)
    coast_eff = round(coast_eff,2)
    print("Your total coast time was {} minutes. You were coasting approximately {}% of the time.".format(coast_time,coast_eff))
    return round(coast_eff,2)