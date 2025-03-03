# Mobile2Cyber Demo - Flake8 Alert Generator
# Código diseñado para mostrar múltiples alertas comunes de Flake8

import os, sys  # E401: Múltiples imports en misma línea

def  bad_spacing( ):  # E202: Espacio antes de paréntesis
    x=5*3+2  # E225: Operador sin espacios
    y = [1,2,3,4 ]  # E231: Falta espacio después de coma, E201: Espacio final
    z = {'key':'value'}  # E231, E203
    if x>3:print("Hola")  # E701: Múltiples declaraciones en línea
    
def duplicate_code():
    a = 10
    a = 10  # F841: Variable duplicada
    
def long_line():

    # E501: Línea de 90+ caracteres (https://example.com/this-is-a-very-long-url-designed-to-trigger-flake8-line-length-violation-example)
    print("Esta línea excede deliberadamente el límite de 79 caracteres para demostrar la violación E501 de Flake8")

def security_issues(password):
    if password == "123456":  # S105: Contraseña hardcodeada
        return True
    
def unused_vars():
    unused = "No se usa"  # F841
    return 5

def type_check():
    num = "5"
    if num is 5:  # E714: Comparación con 'is' para literal
        pass

class  EmptyClass:  # E302: 2 espacios antes de clase
    pass

# W391: Línea en blanco al final
