from pydot import *

import  pydot

from ComplementFunc import *


##
##
##7
row1 = ['|', '|', '|', '|', '|', '|', '|']
##5
row2 = ['|', '|', '|', '|', '|']
##3
row3 = ['|', '|', '|' ]
##
##


#______________________________________________________________________________
# Minimax Search

def minimax_decision(state, game):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states. [Fig. 5.3]"""

    player = game.to_move(state)

    def max_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -infinity
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a)))
        return v

    def min_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = infinity
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a)))
        return v

    # Body of minimax_decision:
    if player == 'M':
        return argmax(game.actions(state),
                      lambda a: min_value(game.result(state, a)))
    else:
        return argmin(game.actions(state),
                      lambda a: max_value(game.result(state, a)))




#CLASS NIMGAME

class Game():

    def __init__(self, sticks, player):

        update(self, sticks = sticks)
        #moves = if_(sticks > 3, [x for x in range(1, 4)],[x for x in range(1,sticks)])



        if (sticks > 3):

            moves = [x for x in range(1,4)]

        else:

            moves = [x for x in range(1,sticks)]


        self.initial = Struct(to_move = "H", utility = 0, sticks = sticks, moves = moves)

    def actions(self, state):
        return state.moves

    def result(self, state, move):
        if move not in state.moves:

            struct = Struct(

                to_move=if_(state.to_move == 'H', 'M', 'H'),

                utility = state.utility,

                sticks = state.sticks,

                moves = state.moves)

            return struct


            #return Struct(to_move=if_(state.to_move == 'H', 'M', 'H'), utility = state.utility, sticks = state.sticks,
                      #moves = state.moves)
        #moves = if_(state.sticks - move > 3, [x for x in range(1, 4)],[x for x in range(1,state.sticks - move)])

        if(state.sticks - move > 3):

            moves = [x for x in range(1,4)]



        else:

            moves = [x for x in range(1, state.sticks - move)]



            #print(move)

        #return Struct(to_move=if_(state.to_move == 'H', 'M', 'H'), utility = self.compute_utility(state, move), sticks = state.sticks - move,
        #             moves = moves)

        struct = Struct(to_move=if_(state.to_move == 'H', 'M', 'H'),

                        utility=self.compute_utility(state, move),

                        sticks=state.sticks - move,

                        moves = moves,

                        )


        return struct


    def compute_utility(self, state, move):
        if state.sticks - move == 1:

            if(state.to_move == "M"):

                return  1

            else:

                return -1

            #return if_(state.to_move == 'M', 1, -1)
        else:
            return 0

    def terminal_test(self, state):
        return state.utility != 0 or len(state.moves) == 0

    def utility(self, state, player):
        return if_(player == 'M', state.utility, -state.utility)

    def display(self, state):
        print ('( %s, %d )' % (state.to_move, state.sticks))



    def to_move(self, state):

    # "Return the player whose move it is in this state."
             return state.to_move

    def __repr__(self):

        return '<%s>' % self.__class__.__name__

def qrow():
    #input row
    return num_or_str(input('input row: '))

def query_player(game, state):
    "Make a move by querying standard input."
    #game.display(state)
    return num_or_str(input('Please, do a moviment:  '))


class Node:
    def __init__(self, state):
        self.state = state
        self.children = []
        self.movevalue = 0

#make tree using minimax

def makeTreeMinimax(root, game):

    player = game.to_move(root.state)

    def max_value(node, state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -infinity
        for a in game.actions(state):
            node.children.append(Node(game.result(state, a)))
            node.children[a - 1].state.utility = min_value(node.children[a - 1],game.result(state, a))
            v = max(v, node.children[a - 1].state.utility)
        node.state.utility = v
        return v

    def min_value(node, state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = infinity
        for a in game.actions(state):
            node.children.append(Node(game.result(state, a)))
            node.children[a - 1].state.utility = max_value(node.children[a - 1],game.result(state, a))
            v = min(v, node.children[a - 1].state.utility)
        node.state.utility = v
        return v

    if root.state.to_move == 'M':
        max_value(root, root.state)
    else:
        min_value(root, root.state)

    return root

def representTree(root,game):
    id = 1
    mygraph = pydot.Dot(graph_type= 'digraph')
    stack = []
    stackgraph = []
    parent = pydot.Node(id, style='filled', fillcolor= if_(root.state.to_move == 'M', 'red', 'blue'),label = root.state.sticks,
                        xlabel = root.state.utility)
    stackgraph.append(parent)
    stack.append(root)
    while stack != []:
        if id > 1000:
            break
        node = stack.pop(0)
        nodefromstackgraph = stackgraph.pop(0)
        id+=1
        mygraph.add_node(parent)
        if node.children != []:
            for i in node.state.moves:
                childstate = node.children[i-1].state
                stack.append(node.children[i-1])
                nodegraph = pydot.Node(id, style='filled', fillcolor= if_(childstate.to_move == 'M', 'red', 'blue'),label = childstate.sticks,
                                       xlabel = childstate.utility)
                stackgraph.append(nodegraph)
                id+=1
                mygraph.add_node(nodegraph)
                edge = pydot.Edge(nodefromstackgraph, nodegraph, label = i)
                mygraph.add_edge(edge)
    nameofgraph = 'game%d-minimax.png' % game.initial.sticks
    mygraph.write_png(nameofgraph)



def main_play(game):

    state = game.initial

    while(not game.terminal_test(state)):
        #filas=qrow()
        move = query_player(game,state)
        newstate1 = game.result(state, move)
        game.display(newstate1)
        #tableton(filas,move)


        if game.terminal_test(newstate1):
            user = if_(newstate1.utility == 1, 'I', 'You')
            print ('%s Win !!' %user)
            break
        mymove = minimax_decision(newstate1,game)

        print ("My Move : %d" % mymove)
        newstate2 = game.result(newstate1, mymove)
        #tableton(filas,move)
        game.display(newstate2)

        if game.terminal_test(newstate2):
            user = if_(newstate2.utility == 1, 'I', 'You')
            print ('%s Win !!' %user)
            break
        state = newstate2
        
def tableton(qrow,move):
    fseleccionada=qrow
    if(fseleccionada==1):
        for i in range(0,move):
            row1.pop()
    if(fseleccionada==2):
        for i in range(0,move):
            row2.pop()
    if(fseleccionada==3):
        for i in range(0,move):
            row3.pop()
    print(*row1)
    print(*row2)
    print(*row3)