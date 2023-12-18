
import math
import time

#1-D lattice total energy function evaluator class
#
class ExploreMaze:
    mazeMap=None
    act = ['N', 'E', 'S', 'W']
        
    @classmethod  
    def ObjFuct(cls,state):
        start = (10, 10)  
        goal = (1, 1)   
        step = 0
        isArrive = False
        # visited = set()
        visited = []
        visited.append(start)
        for action in state:   
            # 撞牆
            if cls.mazeMap[start][action] == 0:
                break
            if action == 'N':
                tempPosition  = (position[0]-1, position[1])   
            elif action == 'S':
                tempPosition  = (position[0]+1, position[1])   
            elif action == 'W':
                tempPosition  = (position[0], position[1]-1)   
            elif action == 'E':
                tempPosition  = (position[0], position[1]+1)   
                
            # 到達終點
            if tempPosition  == cls.goal:
                isArrive = True
                visited.append(goal)
                break
            
            # 檢查有無回頭
            if tempPosition  in path:
                if cls.directions.index(action) == 3:
                    action = cls.directions[0]
                else:
                    action = cls.act[cls.act.index(action)+1]
                if cls.mazeMap[start][action] == 0:
                    break
                if action == 'N':
                    position = (position[0]-1, position[1])   
                elif action == 'S':
                    position = (position[0]+1, position[1])   
                elif action == 'W':
                    position = (position[0], position[1]-1)   
                elif action == 'E':
                    position = (position[0], position[1]+1)
                # break

            else:
                start = tempStart
            step += 1
            path.append(position)
            
            
        return {"isArrive": isArrive,"step": step}, visited
        

