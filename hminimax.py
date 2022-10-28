from pacman_module.game import Agent, Directions, manhattanDistance
import math


def eval(state):
    """
    Given a pacman game state, 
    returns a score base on the current state (like utility).

    Arguments:
    ----------
    - 'state': the current game state. See FAQ and class 'pacman.GameState'.

    Return:
    -------
    - A score base on the current state (like utility).
    """
    value = state.getScore()
    value -= food_heuristic(state)
    value += ghost_distance(state)
    return value


def food_distances(state):
    """
    Given a pacman game state, 
    returns a list of all manathan distances between Pacman and foods.

    Arguments:
    ----------
    - 'state': the current game state. See FAQ and class 'pacman.GameState'.

    Return:
    -------
    - A list of all manathan distances between Pacman and foods.
    """
    foods = state.getFood()
    pacman_pos = state.getPacmanPosition()
    distances = []
    for i in range(foods.width):
        for j in range(foods.height):
            if foods[i][j]:
                distances.append(manhattanDistance((i, j), pacman_pos))
    return distances


def food_heuristic(state):
    """
    Given a pacman game state, returns a heuristic.

    Arguments:
    ----------
    - 'state': the current game state. See FAQ and class 'pacman.GameState'.

    Return:
    -------
    - A heuristic based on the current state.
    """
    distances = food_distances(state)
    size = len(distances)
    return (sum(distances) / size) if size != 0 else 0


def ghost_distance(state):
    """
    Given a pacman game state, 
    returns the manhattan distance between the ghost and pacman.

    Arguments:
    ----------
    - 'state': the current game state. See FAQ and class 'pacman.GameState'.

    Return:
    -------
    - the manhattan distance between the ghost and pacman.
    """
    return manhattanDistance(
        state.getGhostPosition(1),
        state.getPacmanPosition()
    )


def cutoff(before_state, state, depth):
    """
    Given two pacman game states and the current depth, 
    returns a Boolean based on the two games states.

    Arguments:
    ----------
    - 'state': the current game state. See FAQ and class 'pacman.GameState'.

    Return:
    -------
    - A Boolean based on the two games states.
    """
    return (
        state.getNumFood() < before_state.getNumFood() 
        or depth <= 0 or state.isWin() or state.isLose()
    )


class PacmanAgent(Agent):
    """
    A Pacman agent based on H-Minimax.
    """

    def __init__(self):
        super().__init__()

    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.

        Arguments:
        ----------
        - 'state': the current game state. 
        See FAQ and class 'pacman.GameState'.

        Return:
        -------
        - A legal move as defined in 'game.Directions'.
        """
        distances = food_distances(state)
        min_depth = min(distances)
        depth = min_depth - math.sqrt(min_depth)
        depth = depth if depth > 5 else 5

        _, action = self.minimax(state, True, state, depth)
        return action

    def minimax(self, state, is_max_agent, before_state, depth):
        """
        Given a pacman game state, 
        returns a list of legal moves to solve the search layout.

        Arguments:
        ----------
        - 'state': the current game state. 
        See FAQ and class 'pacman.GameState'.

        Return:
        -------
        - A list of legal moves as defined in 'game.Directions'.
        """
        if cutoff(before_state, state, depth):
            return eval(state), Directions.STOP

        successors = []
        if is_max_agent:
            for next_state, action in state.generatePacmanSuccessors():
                if not before_state == next_state:
                    value, _ = self.minimax(next_state, False, state, depth-1)
                    successors.append((value, action))
            return max(successors)
        else:
            for next_state, action in state.generateGhostSuccessors(1):
                if not before_state == next_state:
                    value, _ = self.minimax(next_state, True, state, depth-1)
                    successors.append((value, action))
            return min(successors)
