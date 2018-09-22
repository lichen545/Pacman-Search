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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState())) --> returns list of tuples [(X,Y,Z),(X2,Y2,Z2),...]
    """
    # create empty list of explored nodes
    explored = []

    # create dictionary to store path(s)
    gameDict = {}
    
    # DFS uses stack so create the structure
    gameStack = util.Stack()

    # Example of node being passed into stack:
    # [(x,y), Direction, Cost]
    # .getStartState() returns (x,y)

    # Push tuple onto stack (will be popped off immediately) using action=Stop and cost=0 to indicate start state
    startNode = (problem.getStartState(), "Stop" , 0)
    gameStack.push(startNode)
    gameDict[startNode] = "Start"

    # While the stack is not empty...
    while not gameStack.isEmpty():
        # Pop node on top of stack -- node will be of type tuple mentioned above
        node = gameStack.pop()

        # Check if popped node is the goal state -- get (x,y) coords from first index in tuple and pass into check function
        xyState = node[0]

        # if the current state is the goal state,
        if problem.isGoalState(xyState):
            #print("GOAL!")
            backwardPath = []
            curr = node

            while not curr == "Start":
                backwardPath.append(curr[1]) # append the action
                curr = gameDict[curr] # get nodes parent 
            
            backwardPath = backwardPath[:-1] # remove "stop" from list of actions
            backwardPath.reverse() # reverse the list to get correct order of action
            return backwardPath # return the list of actions to take
        
        # if here that means we are not in goal state, so check if we have been here before
        if xyState not in explored:
            # if here, state has not been explored, so now add it to explored list
            explored.append(xyState)

            # get children (list of tuples) of current state
            successors = problem.getSuccessors(xyState)

            # push each child node onto stack, then visit the last one added
            for s in successors:
                # get xy coord of child
                tempCoord = s[0]

                if tempCoord not in explored:
                    gameStack.push(s)
                    gameDict[s] = node

    # Return false iff no path found from start to goal
    return False
        

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # create empty list of explored nodes
    explored = []

    # create dictionary to store path(s)
    gameDict = {}
    
    # BFS uses queue so create the structure
    gameQ = util.Queue()

    # Example of node being passed into stack:
    # [(x,y), Direction, Cost]
    # .getStartState() returns (x,y)

    # Push tuple onto queue (will be popped off immediately) using action=Stop and cost=0 to indicate start state
    startNode = (problem.getStartState(), "Stop" , 0)
    gameQ.push(startNode)
    gameDict[startNode] = "Start"

    # While the queue is not empty...
    while not gameQ.isEmpty():
        # Pop node on top of queue -- node will be of type tuple mentioned above
        node = gameQ.pop()

        # Check if popped node is the goal state -- get (x,y) coords from first index in tuple and pass into check function
        xyState = node[0]
        #print "NODE: ", node

        # if the current state is the goal state,
        if problem.isGoalState(xyState):
            #print("GOAL!")
            backwardPath = []
            curr = node

            while not curr == "Start":
                backwardPath.append(curr[1]) # append the action
                curr = gameDict[curr] # get nodes parent
            
            backwardPath = backwardPath[:-1] # remove "stop" from list of actions
            backwardPath.reverse() # reverse the list to get correct order of action
            return backwardPath # return the list of actions to take
        
        # if here that means we are not in goal state, so check if we have been here before
        if xyState not in explored:
            # if here, state has not been explored, so now add it to explored list
            explored.append(xyState)

            # get children (list of tuples) of current state
            successors = problem.getSuccessors(xyState)

            # push each child node onto stack, then visit the last one added
            for s in successors:
                #print "SUCCESSOR: ", s
                # get xy coord of child
                tempCoord = s[0]

                if tempCoord not in explored:
                    gameQ.push(s)
                    gameDict[s] = node
    # Return false iff no path found from start to goal
    return False
                    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # create empty list of explored nodes
    explored = []

    # create dictionary to store path(s)
    gameDict = {}
    
    # UCS uses priority queue so create the structure
    gamePQ = util.PriorityQueue()

    # Example of node being passed into stack:
    # [(x,y), Direction, Cost]
    # .getStartState() returns (x,y)

    # Push tuple into queue (will be popped off immediately) using action=Stop and cost=0 to indicate start state
    startNode = (problem.getStartState(), "Stop" , 0)
    gamePQ.push(startNode,0)
    gameDict[startNode] = "Start"

    # While the queue is not empty...
    while not gamePQ.isEmpty():
        # Pop node on top of queue -- node will be of type tuple mentioned above
        node = gamePQ.pop()

        # Check if popped node is the goal state -- get (x,y) coords from first index in tuple and pass into check function
        xyState = node[0]

        # if the current state is the goal state,
        if problem.isGoalState(xyState):
            #print("GOAL!")
            backwardPath = []
            curr = node

            while not curr == "Start":
                backwardPath.append(curr[1]) # append the action
                curr = gameDict[curr] # get nodes parent
            
            backwardPath = backwardPath[:-1] # remove "stop" from list of actions
            backwardPath.reverse() # reverse the list to get correct order of action
            return backwardPath # return the list of actions to take
        
        # if here that means we are not in goal state, so check if we have been here before
        if xyState not in explored:
            # if here, state has not been explored, so now add it to explored list
            explored.append(xyState)

            # get children (list of tuples) of current state
            successors = problem.getSuccessors(xyState)

            for s in successors:
                # get xy coord of child
                tempCoord = s[0]

                # should be in a function...sorry.. gets cost of path so far by creating list and using getCostOfActions()
                if tempCoord not in explored:
                    parents = [] # temp path to trace each successor's cost
                    curr = s # make current node the successor in question
                    gameDict[s] = node # add successors parent before tracing path

                    while not curr == "Start":
                        parents.append(curr[1]) # append the action
                        curr = gameDict[curr] # get nodes parent
                        #print(curr)
                    
                    parents = parents[:-1] # remove "stop" from list of actions
                    parents.reverse() # reverse the list to get correct order of action  

                    newCost = problem.getCostOfActions(parents) # gets cost 

                    gamePQ.push(s,newCost) # push node and cost into pq
                    
    # Return false iff no path found from start to goal
    return False

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # create empty list of explored nodes
    explored = []

    # create dictionary to store path(s)
    gameDict = {}
    
    # UCS uses priority queue so create the structure
    gamePQ = util.PriorityQueue()

    # Example of node being passed into stack:
    # [(x,y), Direction, Cost]
    # .getStartState() returns (x,y)

    # Push tuple into queue (will be popped off immediately) using action=Stop and cost=0 to indicate start state
    startNode = (problem.getStartState(), "Stop" , 0)
    gamePQ.push(startNode,0)
    gameDict[startNode] = "Start"

    # While the queue is not empty...
    while not gamePQ.isEmpty():
        # Pop node on top of queue -- node will be of type tuple mentioned above
        node = gamePQ.pop()

        # Check if popped node is the goal state -- get (x,y) coords from first index in tuple and pass into check function
        xyState = node[0]

        # if the current state is the goal state,
        if problem.isGoalState(xyState):
            #print("GOAL!")
            backwardPath = []
            curr = node

            while not curr == "Start":
                backwardPath.append(curr[1]) # append the action
                curr = gameDict[curr] # get nodes parent
            
            backwardPath = backwardPath[:-1] # remove "stop" from list of actions
            backwardPath.reverse() # reverse the list to get correct order of action
            return backwardPath # return the list of actions to take
        
        # if here that means we are not in goal state, so check if we have been here before
        if xyState not in explored:
            # if here, state has not been explored, so now add it to explored list
            explored.append(xyState)

            # get children (list of tuples) of current state
            successors = problem.getSuccessors(xyState)

            for s in successors:
                # get xy coord of child
                tempCoord = s[0]

                # should be in a function...sorry.. gets cost of path so far by creating list and using getCostOfActions()
                if tempCoord not in explored:
                    parents = [] # temp path to trace each successor's cost
                    curr = s # make current node the successor in question
                    gameDict[s] = node # add successors parent before tracing path

                    while not curr == "Start":
                        parents.append(curr[1]) # append the action
                        curr = gameDict[curr] # get nodes parent
                        #print(curr)
                    
                    parents = parents[:-1] # remove "stop" from list of actions
                    parents.reverse() # reverse the list to get correct order of action  

                    newCost = problem.getCostOfActions(parents) # gets cost 

                    # f(x) = g(x) + h(x) = newCost + heuristic at that point
                    # 
                    gamePQ.push(s,newCost + heuristic(tempCoord,problem)) # push node and cost + heuristic into pq
                    
    # Return false iff no path found from start to goal
    return False

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
