from grid import Grid
import random

class Solver(): 
    """
    A solver class, to be implemented.
    """
    
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

    def solution_naïve(self, grid):
        c = []
        while grid.is_sorted() == False :
            i = (random.randint(1,grid.m), random.randint(0,grid.n))
            j = (random.randint(1,grid.m), random.randint(0,grid.n))
            if abs(i[0]-j[0]) + abs(i[1]-j[1]) > 1 :
                grid.swap(i,j)
                c.append((i,j))
        return (c,len(c),grid)

s = Solver()
g = Grid( 3, 2 , [[5,2],[3,1],[6,4]])
print(s.solution_naïve(g))
