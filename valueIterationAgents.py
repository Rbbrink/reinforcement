# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*
        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.
          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.policy = util.Counter()
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here

        for x in range(iterations):
            newvalues = self.values.copy()
            for y in self.mdp.getStates():
                maxval = None
                for z in self.mdp.getPossibleActions(y):
                    currentValue = self.computeQValueFromValues(y, z)
                    if (maxval == None or currentValue > maxval):
                        maxval = currentValue
                        self.policy[y] = z #by remembering the actions that came with the highest q value, we can just read it instead of recalculating it in computeActionFromValues 
                if maxval == None:
                    newvalues[y] = 0
                else:
                    newvalues[y] = maxval            
            self.values = newvalues

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
        Compute the Q-value of action in state from the
        value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        totval = 0
        for nextS, prob in self.mdp.getTransitionStatesAndProbs(state,action):
            totval += prob * (self.mdp.getReward(state, action, nextS) + (self.discount * self.values[nextS]))

        return totval
          
    def computeActionFromValues(self, state):
        """
        The policy is the best action in the given state
        according to the values currently stored in self.values.
        You may break ties any way you see fit.  Note that if
        there are no legal actions, which is the case at the
        terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        return self.policy[state]

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

# # valueIterationAgents.py
# # -----------------------
# # Licensing Information:  You are free to use or extend these projects for
# # educational purposes provided that (1) you do not distribute or publish
# # solutions, (2) you retain this notice, and (3) you provide clear
# # attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# # 
# # Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# # The core projects and autograders were primarily created by John DeNero
# # (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# # Student side autograding was added by Brad Miller, Nick Hay, and
# # Pieter Abbeel (pabbeel@cs.berkeley.edu).


# import mdp, util

# from learningAgents import ValueEstimationAgent

# class ValueIterationAgent(ValueEstimationAgent):
#     """
#         * Please read learningAgents.py before reading this.*

#         A ValueIterationAgent takes a Markov decision process
#         (see mdp.py) on initialization and runs value iteration
#         for a given number of iterations using the supplied
#         discount factor.
#     """
#     def __init__(self, mdp, discount = 0.9, iterations = 100):
#         """
#           Your value iteration agent should take an mdp on
#           construction, run the indicated number of iterations
#           and then act according to the resulting policy.

#           Some useful mdp methods you will use:
#               mdp.getStates()
#               mdp.getPossibleActions(state)
#               mdp.getTransitionStatesAndProbs(state, action)
#               mdp.getReward(state, action, nextState)
#               mdp.isTerminal(state)
#         """
#         self.mdp = mdp
#         self.discount = discount
#         self.iterations = iterations
#         self.values = util.Counter() # A Counter is a dict with default 0
#         self.policy = util.Counter()
#         self.newvalues = self.values.copy()

#         # Write value iteration code here
#         "*** YOUR CODE HERE ***"
        
#         for a in mdp.getStates():
#             self.values[(a, 'Q')] = None
#         for x in range(iterations):
#             self.newvalues = self.values.copy()
#             for y in mdp.getStates():
#                 for z in self.mdp.getPossibleActions(y):
#                     self.computeQValueFromValues(y, z)
#             self.values = self.newvalues    

#     def getValue(self, state):
#         """
#           Return the value of the state (computed in __init__).
#         """
#         return self.values[state]


#     def computeQValueFromValues(self, state, action):
#         """
#           Compute the Q-value of action in state from the
#           value function stored in self.values.
#         """
#         "*** YOUR CODE HERE ***"
#         StatesAndProbs = self.mdp.getTransitionStatesAndProbs(state, action)
#         totval = 0
#         for a in StatesAndProbs:
#             (nextstate, prob) = a
#             totval += prob * ((self.discount * self.getValue(nextstate)) + self.mdp.getReward(state, action, nextstate))
#         if (self.newvalues[(state, 'Q')] is None or totval > self.newvalues[(state, 'Q')]):
#             self.newvalues[state] = totval
#             self.newvalues[(state, 'Q')] = totval
#             self.policy[state] = action
#         self.newvalues[(state, action)] = totval
#         return totval

#     def computeActionFromValues(self, state):
#         """
#           The policy is the best action in the given state
#           according to the values currently stored in self.values.

#           You may break ties any way you see fit.  Note that if
#           there are no legal actions, which is the case at the
#           terminal state, you should return None.
#         """
#         "*** YOUR CODE HERE ***"
#         return self.policy[state]

#     def getPolicy(self, state):
#         return self.computeActionFromValues(state)

#     def getAction(self, state):
#         "Returns the policy at the state (no exploration)."
#         return self.computeActionFromValues(state)

#     def getQValue(self, state, action):
#         return self.newvalues[(state, action)]
