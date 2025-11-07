from filaPedidos import filaPedidos

def fazerPedido(pedido):
    '''Exemplo: pedido = {
                            "item": "Pizza Margherita",  
                            "quantidade": 2             
                         } '''
    filaPedidos.put(pedido)
    
    