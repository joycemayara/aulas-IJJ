# Obtenção do valor das notas
primeira_nota = float(input("Digite a primeira nota do usuário: "))
segunda_nota = float(input("Digite a segunda nota do usuário: "))
terceira_nota = float(input("Digite a terceira nota do usuário: "))
quarta_nota = float(input("Digite a quarta nota do usuário: "))

#Cálculo da média
media_notas = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

print(f"Olá, Caique! Sua média é:  {media_notas} pontos")