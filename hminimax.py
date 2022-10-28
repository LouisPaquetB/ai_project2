from audioop import minmax
from pacman_module.game import Agent
from pacman_module.pacman import Directions
from pacman_module.util import Queue, PriorityQueue, manhattanDistance
import math

def eval(state):
    value = state.getScore()
    value -= food_heuristic(state)
    value += ghost_heuristic(state)
    return value

def food_heuristic(state):
    foodGrid = state.getFood()
    pacman_pos = state.getPacmanPosition()
    
    distances = []

    for i in range(foodGrid.width):
        for j in range(foodGrid.height):
            if foodGrid[i][j]:
                distances.append(manhattanDistance((i, j), pacman_pos))
    size = len(distances)
    return sum(distances) / size if size != 0 else 0

def ghost_heuristic(state):
    pacman_position = state.getPacmanPosition()
    ghost_postiton = state.getGhostPosition(1)

    return manhattanDistance(ghost_postiton, pacman_position)


class PacmanAgent(Agent):
    """
    A Pacman agent based on Depth-First-Search.
    """

    def __init__(self):
        """
        Arguments:
        ----------
        - `args`: Namespace of arguments from command-line prompt.
        """
        super().__init__()
        self.moves = []

    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Return:
        -------
        - A legal move as defined in `game.Directions`.
        """
        """foodGrid = state.getFood()
        min_distances = (float("inf"),(-1,-1))
        for i in range(foodGrid.width):
            for j in range(foodGrid.height):
                if foodGrid[i][j]:
                    current_distance = (manhattanDistance((i, j), state.getPacmanPosition()), (i,j))
                    if current_distance[0] < min_distances[0]:
                        min_distances = current_distance
                    elif current_distance[0] == min_distances[0]:
                        tmp1 = len(self.bfs(state,current_distance[1]))
                        tmp2 = len(self.bfs(state,min_distances[1]))
                        #print(str(tmp1) + "  ===  " + str(tmp2))
                        min_distances = current_distance if tmp1 < tmp2 else min_distances

        depth = 0 if not min_distances[0] else manhattanDistance(state.getPacmanPosition(),min_distances[1])"""
        depth = eval(state) - state.getScore()
        depth = depth if depth > 2 else 2
        #print(str(min_distances[1]) + " ==== " + str(depth))
        #print(depth)
        test = food_heuristic(state)
        _, action = self.minimax(state, True,state,5, test)
        return action
    
    def cutoff(self, before_state, state):
        return state.getNumFood() != before_state.getNumFood()


    def minimax(self, state, is_max_agent, before_state, depth, cutoff):
        """
        Given a pacman game state,
        returns a list of legal moves to solve the search layout.

        Arguments:
        ----------
        - `state`: the current game state. See FAQ and class
                   `pacman.GameState`.

        Return:
        -------
        - A list of legal moves as defined in `game.Directions`.
        """
        #print(str(state.getNumFood()) + " === " + str(before_state.getNumFood()))
        #if self.cutoff(before_state,state) or depth == 0 or state.isWin() or state.isLose():
        if math.sqrt(cutoff) > food_heuristic(state) or depth == 0 or state.isWin() or state.isLose():
            return eval(state), Directions.STOP
        
        successors = []
        if is_max_agent:
            for next_state, action in state.generatePacmanSuccessors():
                if not before_state == next_state:
                    value, _ = self.minimax(next_state, False, state,depth-1, cutoff)
                    successors.append((value, action))
            return max(successors)
        else:
            for next_state, action in state.generateGhostSuccessors(1):
                if not before_state == next_state:
                    value, _ = self.minimax(next_state, True,state,depth-1, cutoff)
                    successors.append((value, action))
            return min(successors)

    def bfs(self, state, food):
        path = []
        fringe = Queue()
        fringe.push((state, path))
        closed = set()

        while True:
            if fringe.isEmpty():
                return []

            current, path = fringe.pop()
            if not current.getFood()[food[0]][food[1]]:
                return path

            current_key = (current.getPacmanPosition(),current.getFood())
            if current_key in closed:
                continue
            else:
                closed.add(current_key)

            for successor, action in current.generatePacmanSuccessors():
                fringe.push((successor, path + [action]))

        return path

        
