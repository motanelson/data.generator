print("\033c\033[40;37m\ndata generate")
def saves(names,sizes,n):
    f1=open(names,"w")
    for nn in range(sizes):
        f1.write(str(nn)+" , "+str(n*nn)+"\n")
    f1.close()


saves("my.csv",100,2)