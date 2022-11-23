print("Bem Vindo ao meu Quiz")
answer_user = input("quer comecar? (S/N) ")

if answer_user != "S":
    quit()  
    
print("começando...")

print("Para que serve o Github? \n (A) Para instalar jogos \n (B) Para Guardar seus codigos \n (C) Para ver videos")
answer_1 = input("Resposta: ")

if answer_1 == "B":
    print("Resposta Correta")   
else:
    print("Resposta Incorreta")
                                        
if answer_1 != "B":
    quit("Tente novamente...")
        
print("Pergunta numero 2")

print("Para que serve o Git Desktop?  \n (A)Compra de produtos \n (B)Vender algum produto  \n (C) Interagir com o Vscode")
answer_2 = input("Resposta: ")

if answer_2 == "C":
    print("Resposta Correta")
else: 
    print("Resposta Incorreta")
    
if answer_2 != "C":
    quit("Comece novamente...")
  

    

    
