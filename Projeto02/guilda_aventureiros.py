import random


class Aventureiro:

    def __init__(self, nome, idade, classe):
        self.nome = nome
        self.idade = idade
        self.classe = classe.lower()
        self.vida = 100

    def atacar(self):

        if self.classe == "arcanista":
            ataque = "lançou um feitiço antigo"
            dano = random.randint(20, 35)

        elif self.classe == "guardiao":
            ataque = "desferiu um golpe de escudo"
            dano = random.randint(15, 30)

        elif self.classe == "monge":
            ataque = "usou uma técnica espiritual"
            dano = random.randint(18, 28)

        elif self.classe == "sombrio":
            ataque = "arremessou uma lâmina oculta"
            dano = random.randint(22, 32)

        else:
            ataque = "tentou atacar mas falhou miseravelmente"
            dano = 10

        print(f"{self.nome} atacou e {ataque} causando {dano} de dano!")
        return dano


# criando personagens
heroi1 = Aventureiro("Kael", 120, "arcanista")
heroi2 = Aventureiro("Brutus", 35, "guardiao")
heroi3 = Aventureiro("Liang", 28, "monge")
heroi4 = Aventureiro("Nyx", 22, "sombrio")


print("\n⚔️ SIMULADOR DE COMBATE ⚔️\n")

lutador1 = heroi1
lutador2 = heroi4

print(f"{lutador1.nome} VS {lutador2.nome}\n")


while lutador1.vida > 0 and lutador2.vida > 0:

    input("Pressione ENTER para continuar")

    dano = lutador1.atacar()
    lutador2.vida -= dano

    if lutador2.vida <= 0:
        print(f"\n{lutador2.nome} foi derrotado!")
        break

    dano = lutador2.atacar()
    lutador1.vida -= dano

    print(f"\nVida de {lutador1.nome}: {lutador1.vida}")
    print(f"Vida de {lutador2.nome}: {lutador2.vida}")
    print("------------------------")


if lutador1.vida > 0:
    print(f"\n🏆 {lutador1.nome} venceu a batalha!")
else:
    print(f"\n🏆 {lutador2.nome} venceu a batalha!")