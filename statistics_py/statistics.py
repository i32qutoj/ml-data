def statistics(datafilename):
    datafilename="data/"+datafilename
    datafile=open(datafilename)
    l1=datafile.readline()
    l2=datafile.readline()
    l3=datafile.readline()
    instances=int(l1.split()[1])
    features=int(l2.split()[1])
    labels=int(l3.split()[1])

    i = 0
    total_labels = 0
    while i < int(instances):
        line = datafile.readline()
        line_data = line.rstrip('\n').split(" ")
        j = features
        while j < len(line_data):
            total_labels = total_labels + int(line_data[j])
            j = j + 1
        i = i + 1

    # LCard y Lden
    lcard = float(total_labels)/instances
    lden = float(lcard)/labels

    # LCard y LDen formateado a string
    s_lcard = "%8.4f" % lcard
    s_lden = "%8.4f" % lden

    # Impresion de resultado
    print("\nEl total de labels distintos es: " + str(total_labels) + "\n")
    print("La cardinalidad (LCard) es: " + s_lcard + "\n")
    print("La densidad (LDen) es: " + s_lden + "\n")

    datafile.close()
