while True:
    try: 
        name   = str(input("Inform your name: "))
        age    = int(input("Inform your age: "))
        height = float(input("Inform your height: "))
        print (f"Your name is",name+", you are", age,"years old and you are", height,"m tall.")
        print ("-" * 30)
        print ("Variables Types")
        print (type(name))
        print (type(age))
        print (type(height))
        break
    except ValueError:
        print ("Try again. Make sure to enter the correct values.")

  """ 
  CORREÇÃO
  - f precisa de {}, sem ela, o f fica sem função no código
  - str(input é redundante. O input devolve uma string por padrão

  """
