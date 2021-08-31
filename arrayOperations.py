import copy
from Nodo import *
from collections import deque 
from heapq import heappush, heappop, heapify
import timeit

POSSIBLE_MOVES = ['abaixo', 'acima', 'direita', 'esquerda']

FINAL_STATE = '12345678_'

finalStateArray2D =  [
	['1', '2', '3'], 
	['4', '5', '6'], 
	['7', '8', '_']
]

def returnJoinedMoves(array2D):
	listOfJoinedElements = []
	
	for element in array2D:
		listOfJoinedElements.append(''.join(element))
	
	return ''.join(listOfJoinedElements)

def moveDown(emptySpacePosition, array2D):
	arrayCopy = copy.deepcopy(array2D)
 
	numberBelowEmptySpace = arrayCopy[emptySpacePosition[0] + 1][emptySpacePosition[1]]
	arrayCopy[emptySpacePosition[0]][emptySpacePosition[1]] = numberBelowEmptySpace
	arrayCopy[emptySpacePosition[0] + 1][emptySpacePosition[1]] = '_'

	return returnJoinedMoves(arrayCopy)

def moveLeft(emptySpacePosition, array2D):
	arrayCopy = copy.deepcopy(array2D)
 
	numberLeftEmptySpace = arrayCopy[emptySpacePosition[0]][emptySpacePosition[1] - 1]
	arrayCopy[emptySpacePosition[0]][emptySpacePosition[1]] = numberLeftEmptySpace
	arrayCopy[emptySpacePosition[0]][emptySpacePosition[1] - 1] = '_'
 
	return returnJoinedMoves(arrayCopy)

def moveUp(emptySpacePosition, array2D):
	arrayCopy = copy.deepcopy(array2D)
 
	numberLeftEmptySpace = arrayCopy[emptySpacePosition[0] - 1][emptySpacePosition[1]]
	arrayCopy[emptySpacePosition[0]][emptySpacePosition[1]] = numberLeftEmptySpace
	arrayCopy[emptySpacePosition[0] - 1][emptySpacePosition[1]] = '_'
 
	return returnJoinedMoves(arrayCopy)

def moveRight(emptySpacePosition, array2D):
	arrayCopy = copy.deepcopy(array2D)
 
	numberLeftEmptySpace = arrayCopy[emptySpacePosition[0]][emptySpacePosition[1] + 1]
	arrayCopy[emptySpacePosition[0]][emptySpacePosition[1]] = numberLeftEmptySpace
	arrayCopy[emptySpacePosition[0]][emptySpacePosition[1] + 1] = '_'
 
	return returnJoinedMoves(arrayCopy)

def move(directions, emptySpacePosition, array2D):
	dictOfMoves = {
		'abaixo': moveDown,
		'acima': moveUp,
		'esquerda': moveLeft,
		'direita': moveRight
	}
	
	arrayOfTuples = []
	 
	for direction in directions:
		arrayOfTuples.append((direction, dictOfMoves[direction](emptySpacePosition, array2D)))
 
	return arrayOfTuples

def findEmptySpace(array2D):
	for line, b in enumerate(array2D):
		if ('_' in b):
			empty_space_column = array2D[line].index('_')
			return (line, empty_space_column)
 
def findTile(array2D, tile):
	for line, b in enumerate(array2D):
		if (tile in b):
			empty_space_column = array2D[line].index(tile)
			return (line, empty_space_column)

def makeArray2DFromState(stateString):
	arrayEveryThreeChars = [stateString[i:i+3] for i in range(0, len(stateString), 3)]
	
	array2D = arrayEveryThreeChars

	for index, element in enumerate(arrayEveryThreeChars):
		array2D[index] = [element[i:i+1] for i in range(0, len(element), 1)]

	return array2D
 
def definePossibleDirections(emptySpacePosition):
	line = emptySpacePosition[0]
	column = emptySpacePosition[1]

	impossibleMoves = []
	statePossibleMoves = []
 
	if (line == 0):
		impossibleMoves.append('acima')
	elif (line == 2):
		impossibleMoves.append('abaixo')
	if (column == 0):
		impossibleMoves.append('esquerda')
	elif (column == 2):
		impossibleMoves.append('direita')
	
	for move in POSSIBLE_MOVES:
		if (move not in impossibleMoves):
			statePossibleMoves.append(move)
			
	return statePossibleMoves

def returnPossibleMoves(estado):
	array2D = makeArray2DFromState(estado)
	emptySpacePosition = findEmptySpace(array2D)
	possibleDirections = definePossibleDirections(emptySpacePosition)
	possibleMoves = move(possibleDirections, emptySpacePosition, array2D)
	
	return possibleMoves

def returnPossibleMovesAsNodos(nodo, possibleMoves):	
	listOfNewNodes = []
	
	for possibleMove in possibleMoves:
		listOfNewNodes.append(Nodo(possibleMove[1], nodo, possibleMove[0], nodo.custo + 1))
	
	return listOfNewNodes

def sucessor(estado): 
	return returnPossibleMoves(estado)
	
def expande(nodo):
	possibleMoves = sucessor(nodo.estado)
	newNodes = returnPossibleMovesAsNodos(nodo, possibleMoves)
	
	return newNodes
	# for node in newNodes:
	#   print(node.estado, node.acao)
 
def bfs(estado):
	endState = goBFS(estado)

	return returnListOfMoves(endState)
		
def dfs(estado):
	endState = goDFS(estado)

	return returnListOfMoves(endState)

def astar_hamming(estado):
	endState = goAstarhamming(estado)
	
	return returnListOfMoves(endState)

def astar_manhattan(estado):
	endState = goAstarManhattan(estado)
	
	return returnListOfMoves(endState)



def goDFS(estado):
	explorados = set()
	fronteira = deque([Nodo(estado, None, None, 0)])
	
	while (fronteira):
		v = fronteira.pop()
		explorados.add(v.estado)
	
		if (v.estado == FINAL_STATE):
			print('Nós expandidos DFS: ', len(explorados))
			return v
		
		expandidos = expande(v)
		for nodo in expandidos:
			if nodo.estado not in explorados:
				fronteira.append(nodo)
				explorados.add(nodo.estado)
	
def goBFS(estado):
	explorados = set()
	fronteira = deque([Nodo(estado, None, None, 0)])
	
	while (fronteira):
		v = fronteira.popleft()
		explorados.add(v.estado)
	
		if (v.estado == FINAL_STATE):
			print('Nós expandidos BFS: ', len(explorados))
			return v
		
		expandidos = expande(v)
		for nodo in expandidos:
			if nodo.estado not in explorados:
				fronteira.append(nodo)
				explorados.add(nodo.estado)
 
def returnListOfMoves(endState):
	if (not endState):
		return None

	moves = []
	 
	currentState = endState
	
	while(currentState.pai):
		moves.insert(0, currentState.acao)
		currentState = currentState.pai
	
	return moves

def goAstarhamming(estado):
	explorados = set()
	fronteira = []
 
	heappush(fronteira, (0, Nodo(estado, None, None, 0)))

	while (fronteira):
		v = heappop(fronteira)
		explorados.add(v[1].estado)
		numberOfOutOfPlaceTiles = getAmountOfOutOfPlaceTiles(v[1].estado)
	
		if (v[1].estado == FINAL_STATE):
			print('Nós expandidos A* Hamming: ', len(explorados))
			return v[1]
		
		expandidos = expande(v[1])

		for nodo in expandidos:
			if nodo.estado not in explorados:
				nodo.custo = nodo.custo + numberOfOutOfPlaceTiles
				heappush(fronteira, (nodo.custo, nodo))
				explorados.add(nodo.estado)
		
def goAstarManhattan(estado):
	explorados = set()
	fronteira = []
 
	heappush(fronteira, (0, Nodo(estado, None, None, 0)))

	while (fronteira):
		v = heappop(fronteira)
		explorados.add(v[1].estado)
		remainingSteps = remainingStepsToBeInPlace(v[1].estado)
	
		if (v[1].estado == FINAL_STATE):
			print('Nós expandidos A* Manhattan: ', len(explorados))
			return v[1]
		
		expandidos = expande(v[1])

		for nodo in expandidos:
			if nodo.estado not in explorados:
				nodo.custo = nodo.custo + remainingSteps
				heappush(fronteira, (nodo.custo, nodo))
				explorados.add(nodo.estado)    

def remainingStepsToBeInPlace(estado):	
	array2D = makeArray2DFromState(estado)
		
	stepsToBeInPlace = 0
	
	for char in range(0, 3):
		for i in range (0, 3):
			if (array2D[char%3][i] is not finalStateArray2D[char%3][i]):
				value = array2D[char%3][i]
				rowInFinalState, columnInFinalState = findTile(finalStateArray2D, value)
				stepsToBeInPlace = stepsToBeInPlace + abs(char - rowInFinalState) + abs(i - columnInFinalState)
		
	return stepsToBeInPlace
 

 
def getAmountOfOutOfPlaceTiles(estado):
	array2D = makeArray2DFromState(estado)
 
	numberOfOutOfPlaceTiles = 0
 
	for char in range(0, 3):
		for i in range (0, 3):
			if (array2D[char%3][i] is not finalStateArray2D[char%3][i]):
				numberOfOutOfPlaceTiles = numberOfOutOfPlaceTiles + 1

	return numberOfOutOfPlaceTiles