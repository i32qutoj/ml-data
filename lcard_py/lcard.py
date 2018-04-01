def lcard(datafilename):
    datafilename="data/"+datafilename
    datafile=open(datafilename)
    l1=datafile.readline()
    l2=datafile.readline()
    l3=datafile.readline()
    instances=int(l1.split()[1])
    features=int(l2.split()[1])
    labels=int(l3.split()[1])

    total_columns = int(features) + int(labels)

    while i < int(instances):
        line = datafile.readline()
        line_data = line.rstrip('\n').split(" ")

    print(labels_final)
    datafile.close()
