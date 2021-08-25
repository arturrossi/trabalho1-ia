from arrayOperations import returnPossibleMoves, returnPossibleMovesAsNodos

from Nodo import *

def sucessor(estado): 
  return returnPossibleMoves(estado)
  
def expande(nodo):
  possibleMoves = sucessor(nodo.estado)
  newNodes = returnPossibleMovesAsNodos(nodo, possibleMoves)
  
  for node in newNodes:
    print(node.estado, node.acao)
 
if __name__ == "__main__":
    #print(sucessor('2354_1687'))
    nodoPai = Nodo('2_3541687', '', None, 0)
    expande(nodoPai)