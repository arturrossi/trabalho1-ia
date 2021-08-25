import copy
from Nodo import *

POSSIBLE_MOVES = ['abaixo', 'acima', 'direita', 'esquerda']

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
		listOfNewNodes.append(Nodo(possibleMove[1], nodo, possibleMove[0], 1))
	
	return listOfNewNodes