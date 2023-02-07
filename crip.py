from cryptography.fernet import Fernet
import qrcode

nome = input("Bem-vindo a área de reflorestamento! Qual o seu nome, agente? ")
print("Olá ", nome, "prazer! Para ter acesso ao local, é necessário criar uma senha.")

senha = input("Digite uma palavra-chave que não possua caracteres especiais. ")

print("A senha ", senha, " está correta?")
confirmacao = input("Digite s/n para confirmar. ")
while (confirmacao == 'n'):
  senha = input("Digite uma palavra-chave que não possua caracteres especiais. ")
  confirmacao = input("Digite s/n para confirmar. ")

print("Iremos gerar uma criptografia para assegurar que ninguém além de você terá acesso a mesma.")

chave = Fernet.generate_key()
realizaCriptografia = Fernet(chave)

senhaSegura = realizaCriptografia.encrypt(senha.encode())
print("Com a cripgtografia, sua senha será entendida do seguinte modo pelo sistema ", senhaSegura)
senhaNormal = realizaCriptografia.decrypt(senhaSegura)
print("Mas para nós, a mesma será entendida normalmente, da seguinte forma ", senhaNormal)
print("Para ajudar, iremos gerar um QR Code para você usar para você acessar o local!")
img = qrcode.make(senhaSegura)
type(img)
img.save("acessoQRCode.png")
print("Para acessar o QR Code, basta abrir a imagem que foi gerada.")