#!/usr/bin/env python3

def greet_programmer():
    print("Hello,", end=" ")
    print("programmer", end="!\n")

def greet(name):
    print(f"Hello, {name}!", end="\n")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!", end="\n")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2