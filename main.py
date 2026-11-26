from monitor.cotacao import buscar_cotacao


def main():
    valor = buscar_cotacao("USD")
    print(f"Dólar agora: R$ {valor:.2f}")


if __name__ == "__main__":
    main()