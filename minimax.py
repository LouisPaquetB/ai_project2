from pacman_module.game import Agent, Directions


class PacmanAgent(Agent):
    """
    A Pacman agent based on Minimax.
    """

    def __init__(self):
        super().__init__()

    def get_action(self, state):
        """
        Given a pacman game state, returns a legal move.

        Arguments:
        ----------
        - state: the current game state. See FAQ and class 'pacman.GameState'.

        Return:
        -------
        - A legal move as defined in 'game.Directions'.
        """
        _, action = self.minimax(state, True, state)
        return action

    def utility(self, state):
        """
        Given a terminal game state, returns a score.

        Arguments:
        ----------
        - state: the current game state. See FAQ and class 'pacman.GameState'.

        Return:
        -------
        - A Score based on the current state.
        """
        return state.getScore()

    def terminal_test(self, state):
        """
        Given a game state,
        returns Boolean that specify if the game state is terminal.

        Arguments:
        ----------
        - state: the current game state. See FAQ and class 'pacman.GameState'.

        Return:
        -------
        - A Boolean that specify if the game state is terminal
        """
        return state.isWin() or state.isLose()

    def minimax(self, state, is_max_agent, before_state):
        """
        Given a pacman game state,
        returns a list of legal moves to solve the search layout.

        Arguments:
        ----------
        - 'state': the current game state.
        See FAQ and class 'pacman.GameState'.

        Return:
        -------
        - A list of tuples with a score for the node
        and a legal moves as defined in 'game.Directions'.
        """
        if self.terminal_test(state):
            return self.utility(state), Directions.STOP
        else:
            successors = []
            if is_max_agent:
                for next_state, action in state.generatePacmanSuccessors():
                    if not before_state == next_state:
                        value, _ = self.minimax(next_state, False, state)
                        successors.append((value, action))
                return max(successors)
            else:
                for next_state, action in state.generateGhostSuccessors(1):
                    if not before_state == next_state:
                        value, _ = self.minimax(next_state, True, state)
                        successors.append((value, action))
                return min(successors)
