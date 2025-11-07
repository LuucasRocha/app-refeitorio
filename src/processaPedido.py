from filaPedidos import filaPedidos
import json

def processaPedido():
    pedido_atual = filaPedidos.get()
    try:
        produto_solicitado = pedido_atual["item"]
        qtd = pedido_atual["quantidade"]
        if qtd <= 0:
            return {"status": 400, "mensagem": "Quantidade deve ser maior que zero!"}
        arq = open("../schema/cardapio.json", "r")
        dados_do_cardapio = json.loads(arq.read())
        arq.close()
        for item_no_cardapio in dados_do_cardapio['itens']:
            if item_no_cardapio["nome"].lower() == produto_solicitado.lower():
                valor_unitario = item_no_cardapio["preco"]
                total_a_pagar = valor_unitario * qtd
                return {
                    "status": 200,
                    "mensagem": f"Pedido confirmado! Total: R$ {total_a_pagar:.2f}",
                    "detalhes": {
                        "item": item_no_cardapio["nome"],
                        "quantidade": qtd,
                        "preco_unitario": valor_unitario
                    }
                }
        return {"status": 404, "mensagem": "Item não encontrado no cardápio."}
    except KeyError:
        return {"status": 500, "mensagem": "Preencha todos os campos do pedido!"}