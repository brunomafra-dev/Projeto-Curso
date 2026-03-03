def calcular_rank(vitorias, derrotas):
    saldo = vitorias - derrotas

    if vitorias < 10:
       nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"    
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal" 
    return saldo, nivel

vitorias = 7
derrotas =6

saldo, nivel = calcular_rank(vitorias, derrotas)

print(f"O Herói tem saldo de {saldo} está no nivel de {nivel}")
