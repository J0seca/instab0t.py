#! /usr/bin/python3.7
# -*- coding: utf-8 -*-
import os, sys
from instabot import Bot
from getpass import getpass
from datetime import datetime
import time

#primero lo primero, para limpiar la ventana:
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Opciones del Bot:
bot = Bot(
    filter_users=True,
    filter_private_users=False,
    filter_previously_followed=True,
    filter_business_accounts=True,
    filter_verified_accounts=True,
    max_likes_per_day=200,
    max_follows_per_day=200,
    max_followers_to_follow=2000, #si tiene mas seguidores ignora la cuenta
    min_followers_to_follow=60, #si tiene menos seguidores ignora
    min_media_count_to_follow=10, #si tiene menos de estas publicaciones ignora
    like_delay =10,
    unlike_delay =10,
    follow_delay =30,
    unfollow_delay =30,
    comments_file='comentarios_instab0t.txt',
    comment_delay=60,
    )

#De quien serán los  contactos...
def define_usuarios():
    clear()
    print("""Método de ingreso de usuarios:

    1- Manual.

    2- Por archivo de texto.

    """)
    met_usuarios = input()

    #Ingreso manual:
    if(int(met_usuarios) == 1):
        print("""Indicar usuario o usuarios objetivo separados por una coma.
        Ejemplo: usuario1,usuario2,usuario3
        """)
        user2follow = input()
        user2follow = user2follow.replace(" ","").split(",")
    #Ingreso por archivo:
    elif(int(met_usuarios) == 2):

        #revisamos si existe archivo...
        #Si existe:
        if(os.path.isfile('instab0t.txt')):
            lista_usuarios = open("instab0t.txt", "r")
            lista_usuarios = lista_usuarios.readlines()

            user2follow = []
            #agregando usuarios a la lista:
            for u in lista_usuarios:
                  u = u.strip()
                  user2follow.append(u)

        #Si no se encuentra archivo:
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

    #finalmente devuelve lista con las cuentas a procesar:
    return user2follow

#siguiento seguidores de usuario:

def seg_seguidores():
    usuarios_a_seguir = define_usuarios()
    for user in usuarios_a_seguir:
        print("Dando like a seguidos de: ", user)
        bot.follow_followers(user)
        time.sleep(2)

#siguiento seguidos de usuario:

def seg_seguidos():
    usuarios_a_seguir = define_usuarios()
    for user in usuarios_a_seguir:
        print("Siguiendo a seguidores de: ", user)
        bot.follow_following(user)
        time.sleep(2)

#dando likes a ultima publicacion:

def mg_ult_publ(cant):
    usuarios_a_seguir = define_usuarios()
    for user in usuarios_a_seguir:
        print("Dando ", str(cant), " likes a ", user)
        bot.like_user(user, amount=int(cant), filtration=False)
        time.sleep(2)

def opciones():
    clear()
    #imprimimos la challa:
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

    3- Like a últimas publicaciones de usuario.

    4- Like a última publicación de seguidores.

    5- Comentar última publicación de seguidores.

    6- Dar like a ultimas publicaciones de uno o mas hashtag.

    7- Salir.
    """, "-"*40)

    opcion = input("[┐∵]┘ --> Ingrese opción:")

    #Llamamos a funcion dependiendo de opción.
    if(int(opcion) == 1):
        seg_seguidores()
        print("\n\n Proceso terminado!, Enter para volver al menú principal.")
        input()
        opciones()
    elif(int(opcion) == 2):
        seg_seguidos()
        print("\n\n Proceso terminado!, Enter para volver al menú principal.")
        input()
        opciones()
    elif(int(opcion) == 3):
        clear()
        cant_mg = input(" Ingrese cantidad de publicaciones a dar like: ")
        print("Dando Like a ", str(cant_mg), " última(s) publicación(es)!")
        mg_ult_publ(cant_mg)
        print("\n\n Proceso terminado!, Enter para volver al menú principal.")
        input()
        opciones()

    elif(int(opcion) == 4):
        clear()
        Print("Recolectando seguidores de usuario...")
        time.sleep(2)
        seguidores_like = get_user_followers(usuario)
        print("Total de usuarios en archivo: ", str(len(seguidores_like)))

        for seguidor in seguidores_like:
            bot.like_user(seguidor)

        print("\n\n Proceso terminado!, Enter para volver al menú principal.")
        input()
        opciones()

    elif(int(opcion) == 5):
        clear()
        seguidores_like = define_usuarios()
        print("Total de usuarios en archivo:", str(len(seguidores_like)))
        print("\nIniciando proceso...\n")

        if(not os.path.isfile('instab0t_comentarios.txt')):
            print("\nArchivo de comantarios no existe!. Creando archivo: isntab0t_comentarios.txt")
            arch_comentarios = open("instab0t_comentarios.txt","w")
            arch_comentarios.write("Buena foto!\n")
        else:
            arch_comentarios = open("instab0t_comentarios.txt","r")
            arch_comentarios = arch_comentarios.readlines()
            if(len(arch_comentarios) == 0):
                print("\nArchivo de comentarios vacío. Volviendo a menú.")
            else:
                print("Iniciando proceso de comantarios...")
                for seguidor in seguidores_like:
                    bot.comment_user(seguidor)
        print("\n\n Proceso terminado!, Enter para volver al menú principal.")
        input()
        opciones()


    elif(int(opcion) == 6):
        clear()
        print("""Indicar hashtag separados por una coma. (puede ser con o sin #)
            Ejemplo: hastag1,hashtag2,#hashtag3
            """)
        hash2like = input()
        cant_hash = input("\nIngrese total de likes a dar por hashtag: ")
        hash2like = hash2like.replace(" ","").replace("#","").split(",")
        for hashtag in hash2like:
            bot.like_hashtag(hashtag, amount=cant_hash)
        print("\n\n Proceso terminado!, Enter para volver al menú principal.")
        input()
        opciones()

    elif(int(opcion) == 7):
        clear()
        print("Saliendo de programa! [∵]┘")
        time.sleep(1)
        exit()
    else:
        print("Error: Debe elegir una opción válida!")
        time.sleep(2)
        opciones()


def main(bot):
    clear()

    print("""
     _         _        _     __  _
    (_)_ _  __| |_ __ _| |__ /  \| |_
    | | ' \(_-<  _/ _` | '_ \ () |  _|
    |_|_||_/__/\__\__,_|_.__/\__/ \__|...[┐∵]┘
    ""","-"*40)
    time.sleep(1)
    #ingresamos usuario y contraseña desde consola.
    #Tambien puede dejarse el login fijo comentando lineas de abajo
    #y habilidanto las siguientes:
    #(modificamos el contenido interior de las comillas)

    #usuario = input("Ingrese su nombre de usuario:\n")
    #password = getpass("Ingrese contraseña:\n")

    #usuario fijo:
    usuario = 'yagami44686'
    password = 'corollake35'

    clear()

    print("Iniciando sesión... \n\n Log:\n")
    time.sleep(1)
    #Ingresando a IG:
    bot.login(username=usuario, password=password) #tambien podemos agregar proxy=''

    opciones()

#Y al final, El principio...
main(bot)
