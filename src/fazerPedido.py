from filaPedidos import filaPedidos

def fazerPedido(pedido):
    '''Exemplo: pedido = {
                            "item": "Pizza Margherita",  # Nome do item
                            "quantidade": 2             # Quantidade
                         } '''
    filaPedidos.put(pedido)
    
    