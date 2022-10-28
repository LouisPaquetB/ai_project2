from audioop import minmax
from pacman_module.game import Agent
from pacman_module.pacman import Directions
from pacman_module.util import Queue, PriorityQueue, manhattanDistance
import math

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
        value, action = self.minimax(state, True,state,float("-inf"))
        return action

    def utility(self, state):
        return state.getScore()

    def minimax(self, state, is_max_agent, before_state, before_value):
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
        if state.isWin() or state.isLose():
            return self.utility(state), Directions.STOP
        
        successors = []
        if is_max_agent:
            prec_val = float("-inf")
            for next_state, action in state.generatePacmanSuccessors():
                if not before_state == next_state:
                    value, _ = self.minimax(next_state, False, state, prec_val)
                    if value < before_value:
                        return float("-inf"), Directions.STOP
                    else:
                        successors.append((value, action))

            return max(successors)
        else:
            prec_val = float("inf")
            for next_state, action in state.generateGhostSuccessors(1):
                if not before_state == next_state:
                    value, _ = self.minimax(next_state, False, state, prec_val)
                    if value < before_value:
                        return float("inf"), Directions.STOP
                    else:
                        successors.append((value, action))

            return min(successors)

        
from audioop import minmax
from pacman_module.game import Agent
from pacman_module.pacman import Directions
from pacman_module.util import Queue, PriorityQueue, manhattanDistance
import math

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
        value, action = self.minimax(state, True,state,float("-inf"))
        return action

    def utility(self, state):
        return state.getScore()

    def minimax(self, state, is_max_agent, before_state, before_value):
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
        if state.isWin() or state.isLose():
            return self.utility(state), Directions.STOP
        
        successors = []
        if is_max_agent:
            prec_val = float("-inf")
            for next_state, action in state.generatePacmanSuccessors():
                if not before_state == next_state:
                    value, _ = self.minimax(next_state, False, state, prec_val)
                    if value < before_value:
                        return float("-inf"), Directions.STOP
                    else:
                        successors.append((value, action))

            return max(successors)
        else:
            prec_val = float("inf")
            for next_state, action in state.generateGhostSuccessors(1):
                if not before_state == next_state:
                    value, _ = self.minimax(next_state, False, state, prec_val)
                    if value < before_value:
                        return float("inf"), Directions.STOP
                    else:
                        successors.append((value, action))

            return min(successors)

        
