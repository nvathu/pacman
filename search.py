"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys
from time import sleep

from game import Directions

n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def depthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    Frontier = util.Stack()
    expand = []
    Frontier.push((problem.getStartState(),[]))
    while not Frontier.isEmpty():
        current_state , current_path = Frontier.pop()
        
        if problem.isGoalState(current_state):
            break
        else:
            if current_state in expand:
                continue
            else:
                expand.append(current_state)
                for next_state in problem.getSuccessors(current_state)[::-1]:
                    Frontier.push((next_state[0], current_path + [next_state[1]] ))
    return current_path
    # TODO


def breadthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    Frontier = util.Queue()
    expand = []
    Frontier.push((problem.getStartState(),[]))
    while not Frontier.isEmpty():
        current_state , current_path = Frontier.pop()
        
        if problem.isGoalState(current_state):
            break
        else:
            if current_state in expand:
                continue
            else:
                expand.append(current_state)
                for next_state in problem.getSuccessors(current_state):
                    Frontier.push((next_state[0], current_path + [next_state[1]] ))
    return current_path
    # TODO


def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    Frontier = util.PriorityQueue()   
    expand = []  
    Frontier.push((problem.getStartState(), [], 0), 0)   
    while not Frontier.isEmpty():
        current_state = Frontier.pop()
        if problem.isGoalState(current_state[0]):
            break
        else:
            if current_state[0] in expand: 
                continue
            else:
                expand.append(current_state[0])  
                for next_state in problem.getSuccessors(current_state[0]):
                    Frontier.push((next_state[0], current_state[1] + [next_state[1]], current_state[2] + next_state[2]), current_state[2] + next_state[2])  
    return current_state[1]
    # TODO


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    '''
    return a path to the goal
    '''
    Frontier = util.PriorityQueue()   
    expand = []   
    Frontier.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(),problem) + 0)
    # while not Frontier.isEmpty():
    #     current_state = Frontier.pop()
    #     if problem.isGoalState(current_state[0]):
    #         #return (current_state[1] + heuristic(current_state[0],problem))
    #         break
    #     else:
    #         continue
    #     if current_state[0] in expand:
    #         continue
    #     else:
    #         expand.append(current_state[0])

    #     if not (problem.getSuccessors(current_state[0]) is None):
    #         for next_state in problem.getSuccessors(current_state[0]):
    #             if next_state[1] in expand:
    #                 continue
    #             else:
    #                 Frontier.push((next_state[0], current_state[1] + [next_state[1]], current_state[2] + next_state[2]), current_state[2] + next_state[2] + heuristic(next_state[0],problem)) 
    while not Frontier.isEmpty():
        current_state = Frontier.pop()
        if problem.isGoalState(current_state[0]):
            break
        else:
            if current_state[0] in expand: 
                continue
            else:
                expand.append(current_state[0])  
                for next_state in problem.getSuccessors(current_state[0]):
                    Frontier.push((next_state[0], current_state[1] + [next_state[1]], current_state[2] + next_state[2]), current_state[2] + next_state[2]  + heuristic(next_state[0],problem))  
    return current_state[1]
    
    # TODO


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch