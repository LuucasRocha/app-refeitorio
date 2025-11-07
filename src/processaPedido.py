from filaPedidos import filaPedidos
import json

def processaPedido():
    pedido = filaPedidos.get()
    arq = open("./schema/cardapio.json", "r")
    dadosCardapio = json.loads(arq.read())
    arq.close()
    try:
        item_pedido = pedido["item"]
        quantidade = pedido["quantidade"]
        for item in dadosCardapio['itens']:
            if item["nome"].lower() == item_pedido.lower():
                preco_total = item["preco"] * quantidade
                return {"status": 200, "mensagem": f"Pedido confirmado! Total: R$ {preco_total:.2f}", "detalhes": {"item": item["nome"], "quantidade": quantidade, "preco_unitario": item["preco"]}}
        return {"status": 404, "mensagem": "Item não encontrado no cardápio."}
    except KeyError:
        return {"status": 500, "mensagem": "Preencha todos os campos do pedido!"}