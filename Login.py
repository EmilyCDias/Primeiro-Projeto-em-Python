usuario = "rmd"
senha = "025b"

Digite_usuario = input("Digite login: \n")
Digite_senha = input("Senha: \n")

if Digite_usuario == usuario and Digite_senha == senha:
    print("Senha correta")
elif Digite_usuario != usuario:
    print("Usuário incorreto.")
elif Digite_senha != senha:
    print("Senha errada.")
else:
    print("Acesso bloqueado.")
