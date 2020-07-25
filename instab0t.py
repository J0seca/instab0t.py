#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from instabot import Bot
from getpass import getpass
from datetime import datetime
import time

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def define_usuarios():
    clear()
    print("""Método de ingreso de usuarios:

    1- Manual.

    2- Por archivo de texto.

    """)
    met_usuarios = input()
    if(int(met_usuarios) == 1):
        print("""Indicar usuario o usuarios objetivo separados por una coma.
        Ejemplo: usuario1,usuario2,usuario3
        """)
        user2follow = input()
        user2follow = user2follow.replace(" ","").split(",")
    elif(int(met_usuarios) == 2):

        if(os.path.isfile('instab0t.txt')):
            lista_usuarios = open("instab0t.txt", "r")
            lista_usuarios = lista_usuarios.readlines()

            user2follow = []
            for u in lista_usuarios:
                  u = u.strip()
                  user2follow.append(u)

        else:
            clear()
            print("""No se encontró archivo!

                Creando archivo instab0t.txt

                IMPORTANTE: El archivo debe tener una columna con un usuario por fila.

                Ejemplo:

                usuari01
                usuari02
                usuari03

                """)
            open("instab0t.txt","w")
            print("Archivo creado!, presione cualquier tecla para continuar.")
            input()
            exit()
    else:
        print("Opción incorrecta!")
        time.sleep(2)
        define_usuarios()
    return user2follow

#siguiento seguidores de usuario:

def seg_seguidores():
    usuarios_a_seguir = define_usuarios()
    for user in usuarios_a_seguir:
        #bot.follow_following(user)
        print("Dando like a seguidor: ", user)
        time.sleep(2)

#siguiento seguidos de usuario:

def seg_seguidos():
    usuarios_a_seguir = define_usuarios()
    for user in usuarios_a_seguir:
        #bot.follow_followers(user)
        print("Dando Siguiendo a seguido: ", user)
        time.sleep(2)

#dando likes a ultima publicacion:

def mg_ult_publ(cant):
    usuarios_a_seguir = define_usuarios()
    for user in usuarios_a_seguir:
        #bot.like_user(user, amount=cant, filtration=False)
        rint("Dando like a: ", user)
        time.sleep(2)

def opciones():
    clear()
    print("""
      ___           _  __              _
     / _ \ _ __  __(_)/  \ _ _  ___ __(_)
    | (_) | '_ \/ _| | () | ' \/ -_|_-<_
     \___/| .__/\__|_|\__/|_||_\___/__(_) ... └[∵]┘
          |_|
    """, "-"*40)

    print("""
    1- Seguir *seguidores* de uno o varios usuarios.

    2- Seguir *seguidos* por uno o varios usuarios.

    3- Like a ultima publicación de usuarios.

    4- Salir.
    """, "-"*40)

    opcion = input("[┐∵]┘ --> Ingrese opción:")

    if(int(opcion) == 1):
        seg_seguidores()
        print("\n\n Proceso terminado!, Enter para volver al menu.")
        input()
        opciones()
    elif(int(opcion) == 2):
        seg_seguidos()
        print("\n\n Proceso terminado!, Enter para volver al menu.")
        input()
        opciones()
    elif(int(opcion) == 3):
        clear()
        cant_mg = input(" Ingrese cantidad de MG a dar: ")
        print("Dando Me Gusta a ultima(s) publicación(es)!")
        mg_ult_publ(cant_mg)
        print("\n\n Proceso terminado!, Enter para volver al menu.")
        input()
        opciones()
        print("Proceso finalizado!")
        time.sleep(2)
        opciones()
    elif(int(opcion) == 4):
        clear()
        print("Saliendo de programa! [∵]┘")
        time.sleep(1)
        exit()
    else:
        print("Error: Debe elegir una opción válida!")
        time.sleep(2)
        opciones()


clear()
print(""" _         _        _     __  _
(_)_ _  __| |_ __ _| |__ /  \| |_
| | ' \(_-<  _/ _` | '_ \ () |  _|
|_|_||_/__/\__\__,_|_.__/\__/ \__|...[┐∵]┘
""","-"*40)

usuario = input("Ingrese su nombre de usuario:\n")
password = getpass("Ingrese contraseña:\n")

clear()

print("Creando Bot e iniciando sesión... \n\n Log:\n")
time.sleep(1)
bot = Bot(
    filter_users=True,
    filter_private_users=False,
    filter_previously_followed=True,
    filter_business_accounts=True,
    filter_verified_accounts=True,
    )
#bot.login(username=usuario, password=password) #tambien podemos agregar proxy=''

opciones()
