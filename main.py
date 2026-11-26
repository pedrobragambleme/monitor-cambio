from monitor.cotacao import buscar_cotacao
from monitor import banco


def main():
    moeda = "USD"
    valor = buscar_cotacao(moeda)
    print(f"Dólar agora: R$ {valor:.2f}")

    con = banco.conectar()
    banco.salvar(con, moeda, valor)

    historico = banco.listar(con, moeda)
    print(f"\nHistórico ({len(historico)} registros):")
    for data_hora, v in historico:
        print(f"  {data_hora}  R$ {v:.2f}")

    con.close()


if __name__ == "__main__":
    main()