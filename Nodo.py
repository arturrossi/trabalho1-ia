class Nodo:
  def __init__(self, estado, pai, acao, custo):
    self.estado = estado
    self.pai = pai
    self.acao = acao
    self.custo = custo
    
  def __lt__(self, other):
    return self.custo < other.custo