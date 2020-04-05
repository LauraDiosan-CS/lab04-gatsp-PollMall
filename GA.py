from Cromozom import Cromozom
from random import random
from math import sqrt

class GA:
    def __init__(self,path):
        self.__path=path
        self.__param=self.__read_data_eil51()
        self.__generation=self.__init_generation()

    def __evaluate(self,repr):
        fitness=0.0
        for i in range(len(repr)-1):
            fitness+=self.__param['mat'][repr[i]][repr[i+1]]
        fitness+=self.__param['mat'][repr[-1]][repr[0]]
        return fitness

    def __init_generation(self):
        c1=Cromozom(self.__param['noNodes'])
        c1.init_cromo()
        c1.fitness=self.__evaluate(c1.repr)
        c2=Cromozom(self.__param['noNodes'])
        c2.init_cromo()
        c2.fitness=self.__evaluate(c2.repr)
        c3=Cromozom(self.__param['noNodes'])
        c3.init_cromo()
        c3.fitness=self.__evaluate(c3.repr)
        c4=Cromozom(self.__param['noNodes'])
        c4.init_cromo()
        c4.fitness=self.__evaluate(c4.repr)
        return [c1,c2,c3,c4]

    def __choose_parent(self):
        chances=self.__chances()
        val=random()
        if val<chances[0]:
            return self.__generation[0]
        elif val<chances[0]+chances[1]:
            return self.__generation[1]
        elif val<chances[0]+chances[1]+chances[2]:
            return self.__generation[2]
        return self.__generation[3]

    def __chances(self):
        chances=[]
        sum=0
        for c in self.__generation:
            sum+=(self.__param['total']-c.fitness)
        for c in self.__generation:
            chances.append((self.__param['total']-c.fitness)/sum)
        return chances

    def __best_cromo(self,generation):
        best=generation[0]
        for c in generation:
            if c.fitness<best.fitness:
                best=c
        return best
    
    def __worst_cromo(self,generation):
        worst=generation[0]
        for c in generation:
            if c.fitness>worst.fitness:
                worst=c
        return worst

    def __one_generation(self):
        for _ in range(len(self.__generation)):
            p1=self.__choose_parent()
            p2=self.__choose_parent()
            c1=p1.crossover(p2)
            c1.mutation()
            c1.fitness=self.__evaluate(c1.repr)
            c2=p2.crossover(p1)
            c2.mutation()
            c2.fitness=self.__evaluate(c2.repr)
            best=self.__best_cromo([c1,c2])
            worst=self.__worst_cromo(self.__generation)
            if best.fitness<worst.fitness:
                index=self.__generation.index(worst)
                self.__generation[index]=best
    def resolve(self):
        nr_generation=0
        prev_best=self.__best_cromo(self.__generation)
        while nr_generation!=10000:
            self.__one_generation()
            current_best=self.__best_cromo(self.__generation)
            if current_best.fitness<prev_best.fitness:
                prev_best=current_best
                nr_generation=-1
            print(current_best.fitness)
            nr_generation+=1
        self.__write_data(prev_best)
        return prev_best

    def __read_data(self):
        sum=0
        with open(self.__path, "r") as file:
            noNodes = int(file.readline())
            mat=[]
            for _ in range(noNodes):
                line=file.readline()
                mat.append([])
                numbers = line.split(",")
                for nr in numbers:
                    mat[-1].append(int(nr))
                    sum+=int(nr)
        return {'noNodes':noNodes,'mat':mat,'total':sum}

    def __read_data_eil51(self):
        d=dict()
        nr_nodes=0
        sum=0
        with open(self.__path,'r') as file:
            for _ in range(6):
                file.readline()
            line=file.readline()
            while (line)!="EOF":
                values=line.split(" ")
                node=int(values[0])
                x=int(values[1])
                y=int(values[2])
                if node not in d:
                    d[node]=[x,y]
                nr_nodes+=1
                print(line)
                line=file.readline()
        mat=[[0 for _ in range(nr_nodes)]
            for _ in range(nr_nodes)]
        print(d)
        for key_i in d:
            for key_j in d:
                x_i=d[key_i][0]
                y_i=d[key_i][1]
                x_j=d[key_j][0]
                y_j=d[key_j][1]
                dist=sqrt((x_i-x_j)**2+(y_i-y_j)**2)
                sum+=dist
                mat[key_i-1][key_j-1]=dist
        return {'noNodes':nr_nodes,'mat':mat,'total':sum}



    def __write_data(self,best):
        file_name=self.__path.split('.')[0]+'_solution.txt'
        with open(file_name,'w') as file:
            file.write(str(self.__param['noNodes'])+'\n')
            for i in range(len(best.repr)-1):
                file.write(str(best.repr[i]+1)+',')
            file.write(str(best.repr[-1]+1)+'\n')
            file.write(str(best.fitness)+'\n')