from random import randint

class Cromozom:
    def __init__(self,noNodes):
        self.__noNodes=noNodes
        self.__repr=[]
        self.__fitness=0.0

    def __get_repr(self):
        return self.__repr

    def __set_repr(self,repr):
        self.__repr=repr

    def __get_fitness(self):
        return self.__fitness

    def __set_fitness(self,fitness):
        self.__fitness=fitness

    repr=property(__get_repr,__set_repr)
    fitness=property(__get_fitness,__set_fitness)

    def init_cromo(self):
        c=[i for i in range(self.__noNodes)]
        for i in range(self.__noNodes):
            index=randint(0,self.__noNodes-1)
            c[i],c[index]=c[index],c[i]
        self.__repr=c

    def crossover(self,c):
        index_st=randint(0,self.__noNodes-1)
        index_dr=randint(0,self.__noNodes-1)
        if index_st>index_dr:
            index_st,index_dr=index_dr,index_st
        d=[None for _ in range(0,self.__noNodes)]
        #p1
        for i in range(index_st,index_dr+1):
            d[i]=self.__repr[i]
        #p2
        i=index_dr+1
        j=index_dr+1
        while None in d:
            while c.repr[j%self.__noNodes] in d:
                j+=1
            d[i%self.__noNodes]=c.repr[j%self.__noNodes]
            i+=1

        child=Cromozom(self.__noNodes)
        child.repr=d
        return child

    def mutation(self):
        for _ in range(self.__noNodes//5):
            index_st=randint(0,self.__noNodes-1)
            index_dr=randint(0,self.__noNodes-1)
            if index_st>index_dr:
                index_st,index_dr=index_dr,index_st
            self.__repr[index_st],self.__repr[index_dr]=self.__repr[index_dr],self.__repr[index_st]

    def __str__(self):
        return 'Cromozomul: '+str(self.__repr)+' ; fitness: '+str(self.__fitness)