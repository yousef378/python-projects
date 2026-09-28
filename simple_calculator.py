while True:
  numper_1=int(input("please type numper:"))
  numper_2=int(input("please type numper:"))
  a=input("please chouse + or - or * or /:")


  def calce(n1,n2):
      if a == "+":
        print(n1 + n2)
      elif a == "-":
        print(n1 - n2)
      elif a == "*":
        print(n1 * n2)
      elif a == "/" and numper_2 != 0 :
        print(n1 / n2)
      else:
        print ("erorr")
  calce(numper_1,numper_2)
    