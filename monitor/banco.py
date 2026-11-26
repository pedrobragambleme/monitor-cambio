import sqlite3
from datetime import datetime

ARQUIVO = "cotacoes.db"


def conectar(arquivo=ARQUIVO):
    con = sqlite3.connect(arquivo)
    con.execute("""
        CREATE TABLE IF NOT EXISTS cotacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moeda TEXT NOT NULL,
            valor REAL NOT NULL,
            data_hora TEXT NOT NULL
        )
    """)
    return con


def salvar(con, moeda, valor):
    agora = datetime.now().isoformat(timespec="seconds")
    con.execute(
        "INSERT INTO cotacoes (moeda, valor, data_hora) VALUES (?, ?, ?)",
        (moeda, valor, agora),
    )
    con.commit()


def listar(con, moeda):
    return con.execute(
        "SELECT data_hora, valor FROM cotacoes WHERE moeda = ? ORDER BY data_hora",
        (moeda,),
    ).fetchall()