# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    if problem.isGoalState(problem.getStartState()):
        return []
    frontier = util.Stack()
    v_d = {}

    frontier.push((problem.getStartState(), [], 0)) #frontier is a list of triples
    
    while frontier.isEmpty != True:
        
        popped = frontier.pop()
        curr_state = popped[0] #popped a list element
        curr_path = popped[1]
        curr_cost = popped[2] 
        if curr_state not in v_d: #cycle checking by storing the states that we have visited so far
            v_d[curr_state] = "V"
            if problem.isGoalState(curr_state):
                return curr_path
            for i in problem.getSuccessors(curr_state): #pulling the list of all successors of the current node one-by-one
                success_state = i[0] #popped a list element
                action = i[1]
                success_cost = i[2]
                new_path = curr_path + [action]
                frontier.push((success_state, new_path,curr_cost+success_cost))
    #util.raiseNotDefined()

# def pathChecking(paths):
#     """A function used to perform path checking"""
#     #print("Paths inside the helper:", paths)
#     check = []
#     for i in paths:
#         check.append(i)
#     return len(check) != len(set(check))    

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    if problem.isGoalState(problem.getStartState()):
        return []
    frontier = util.Queue()
    v_d = {}

    frontier.push((problem.getStartState(), [], 0)) #frontier is a list of triples
    
    while frontier.isEmpty != True:
        
        popped = frontier.pop()
        curr_state = popped[0] #popped a list element
        curr_path = popped[1]
        curr_cost = popped[2] 
        if curr_state not in v_d: #cycle checking by storing the states that we have visited so far
            v_d[curr_state] = "V"
            if problem.isGoalState(curr_state):
                return curr_path
            for i in problem.getSuccessors(curr_state): #pulling the list of all successors of the current node one-by-one
                success_state = i[0] #popped a list element
                action = i[1]
                success_cost = i[2]
                new_path = curr_path + [action]
                frontier.push((success_state, new_path,curr_cost+success_cost))

        
    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    
    if problem.isGoalState(problem.getStartState()):
        return []
    frontier = util.PriorityQueue()
    v_d = {}

    frontier.push((problem.getStartState(), [], 0), 0) #frontier is a list of triples
    
    while frontier.isEmpty != True:
        
        popped = frontier.pop()
        curr_state = popped[0] #popped a list element
        curr_path = popped[1]
        curr_cost = popped[2] 
        if curr_state not in v_d: #cycle checking by storing the states that we have visited so far
            v_d[curr_state] = "V"
            if problem.isGoalState(curr_state):
                return curr_path
            for i in problem.getSuccessors(curr_state): #pulling the list of all successors of the current node one-by-one
                success_state = i[0] #popped a list element
                action = i[1]
                success_cost = i[2]
                new_path = curr_path + [action]
                frontier.update((success_state, new_path, curr_cost+success_cost), curr_cost+success_cost)
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# def priorityFunction(problem, state, heuristic):
#     print("State is:", state)
#     if len(state)>2:
#         return problem.getCostOfActions(state[1]) + heuristic(state[0],problem)
#     else:
#         return heuristic(state,problem)

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    if problem.isGoalState(problem.getStartState()):
        return []
    frontier = util.PriorityQueue()
    v_d = {}

    frontier.push((problem.getStartState(), [], 0), 0) #frintier is a list of triples

    while frontier.isEmpty != True:
        
        popped = frontier.pop()
        curr_state = popped[0] #popped a list element
        curr_path = popped[1]
        curr_cost = popped[2] 
        if curr_state not in v_d: #cycle checking by storing the states that we have visited so far
            v_d[curr_state] = "V"
            if problem.isGoalState(curr_state):
                return curr_path
            for i in problem.getSuccessors(curr_state): #pulling the list of all successors of the current node one-by-one
                success_state = i[0] #popped a list element
                action = i[1]
                success_cost = i[2]
                new_path = curr_path + [action]
                frontier.update((success_state, new_path, curr_cost+success_cost), curr_cost+success_cost+heuristic(success_state, problem))
    #util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
