import BotMarathon
import BotLuckia
import BotCodere
import pandas as pd
import os


def menu():
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print("-------------------------------------------------------------------------------------------------------------")
    print("MENU BOT BEST")  
    print("")
    print ("Selecciona una opción:")
    print("")
    print ("\t1 - Escanear casas de apuestas")
    print("")
    print ("\t2 - Comparar")
    print("")
    print("\t3 - Apostar")
    print("")
    print ("\t9 - Salir")
    print("-------------------------------------------------------------------------------------------------------------")

while True:
    
    # Mostramos el menu
    
    menu()

    # solicituamos una opción al usuario
    
    opcionMenu = input("Inserta un numero valor y pulsa Enter>> ")

    if opcionMenu == "1":
            os.system('clear') # NOTA para windows tienes que cambiar clear por cls
            print("-------------------------------------------------------------------------------------------------------------")
            print("MENU BOT BEST")  
            print("")
            print ("Selecciona una opción:")
            print("")
            print ("\t1 - Marathon")
            print("")
            print ("\t2 - Luckia")
            print("")
            print("\t3 - Codere")
            print("")
            print ("\t9 - Volver")
            print("-------------------------------------------------------------------------------------------------------------")
                                   
                # solicituamos una opción al usuario
                
            opcionMenu2 = input("Inserta un numero valor y pulsa Enter>> ")
                
            if opcionMenu2 == "1":

                df_Marathon = BotMarathon.Escanear_Partidos_directos()
                df_Marathon = df_Marathon.drop(['Mercado'], axis=1)
                df_Marathon = df_Marathon.drop(['Mercado_1'], axis=1)  
                df_Marathon = df_Marathon.drop(['Mercado_X'], axis=1)
                df_Marathon = df_Marathon.drop(['Mercado_2'], axis=1)
                #Convertir las olumnas a numero flotante
                df_Marathon[["1", "X", "2"]] = df_Marathon[["1", "X", "2"]].apply(pd.to_numeric)
                print(df_Marathon)
                print('------------------------------------------------------------------------------')
                #df_Marathon2=df_Marathon.sort_values(by='1', ascending=False)
                #print(df_Marathon2)
                Maximo=df_Marathon.loc[df_Marathon['1'].idxmax()]
                print(Maximo)

                ##print(df_Marathon.loc[:, '1'].dropna().max())  #Obtinene solo un numero maximo
                #print(Maximo.iloc[0])
                #print(Maximo.iloc[1])
                #print(Maximo.iloc[4])
                #print(Maximo.iloc[5])
                #print(Maximo.iloc[6])
              
                #Apostar el mayor
                try:
                    a=float(Maximo.iloc[4])
                    b=float(Maximo.iloc[5])
                    c=float(Maximo.iloc[6])
                    z=(a/1)+(b/1)+(c/1)

                    if z > 1:
                      
                        BotMarathon.Realizar_apuesta(Maximo.iloc[0] + ' — ' + Maximo.iloc[1], 0.50)

                except:
                    print('Apuesta no realizada...')
                    pass
                
                #BotMarathon.Realizar_apuesta('Sao Bernardo' + ' — ' + 'Agua Santa-SP', 0.50)
                
            elif opcionMenu2 == "2":
                             

                #df_Luckia = BotLuckia.Escanear_Partidos_directos()
                ##Convertir las olumnas a numero flotante
                #df_Luckia[["1", "X", "2"]] = df_Luckia[["1", "X", "2"]].apply(pd.to_numeric)
                ##df_Luckia = BotLuckia.Bestluckia()
                #print(df_Luckia)
                #print('------------------------------------------------------------------------------')
                #df_Luckia2=df_Luckia.sort_values(by='1', ascending=False)
                #print(df_Luckia2)

                ##BotLuckia.Realizar_apuesta(df_Luckia2.iloc[0, 0] + ' — ' + df_Luckia2.iloc[0, 1], 0.20)

                ##Apostar el mayor
                #try:
                #    a=float(df_Luckia2.loc[0, '1'])
                #    b=float(df_Luckia2.loc[0, 'X'])
                #    c=float(df_Luckia2.loc[0, '2'])
                #    z=(a/1)+(b/1)+(c/1)

                #    if z > 1:
                      
                #        BotLuckia.Realizar_apuesta(df_Luckia2.loc[0, 'Local'] + ' — ' + df_Luckia2.loc[0, 'Visitante'], 0.50)

                #except:
                #    print('Apuesta no realizada...')
                #    pass



                #df_Luckia = BotLuckia.Escanear_Partidos_directos()
                ##BotLuckia.Inicio_sesion()
             
                
            elif opcionMenu2 == "3":
            
                BotCodere.BestCodere()
                
                df_Codere = pd.DataFrame(BotCodere.Datos_Codere, columns = ['Local', 'Visitante', 'Tiempo', 'Estado', 'Mercado_1', '1', 'Mercado_X', 'X', 'Mercado_2', '2'])
                
                df_Codere = df_Codere.drop(['Mercado_1'], axis=1)  
                
                df_Codere = df_Codere.drop(['Mercado_X'], axis=1)
                
                df_Codere = df_Codere.drop(['Mercado_2'], axis=1)
                
                print(df_Codere)

            elif opcionMenu2 == "4":
            
                df_Betsson = BotBetsson.BesBetsson()
                print(df_Betsson)
                df2=df_Betsson.sort_values(by='1', ascending=False)
                print(df2)

                
            elif opcionMenu2 == "9":
                
                pass
                
            else:
                
                print("")
                
                input("No has pulsado ninguna opción correcta...\nPulsa Enter para continuar")
                
                break
            
        
        
    elif opcionMenu == "2":
        
        print("")
        print("")
        print("Lo sentimos, este apartado esta en desarrollo.")
        input("Pulsa Enter para continuar >>")
        
        pass
        
    #     # Comparar()
        
        
        
    elif opcionMenu == "3":
        
        print("")
        print("")
        print("Lo sentimos, este apartado esta en desarrollo.")
        input("Pulsa Enter para continuar >>")
        
        pass
        
    #     # Apostar()
        
    elif opcionMenu == "9":
      

        break
    
    else:
        
        print("")
        input("No has pulsado ninguna opción correcta...\nPulsa Enter para continuar")




if __name__ == '__main__':
    menu()
