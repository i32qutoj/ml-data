#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ninstances_py.ninstances import ninstances
from statistics_py.statistics import statistics

def main():
    loop_condition=True

    while loop_condition == True:
        print("\nMenu:\n")
        print("0.- EXIT")
        print("1.- Number of instances, features and labels (Juan A. Romero)")
        print("2.- Statistics (Joaquín Quero Torres - i32qutoj)")

        main_input = int(input())

        if main_input == 0:
            loop_condition = False
            break
        elif main_input == 1:
            datafile=input("Introduce nombre de datafile: ")
            ninstances(datafile)
        elif main_input == 2:
            datafile=input("Introduce nombre de datafile: ")
            statistics(datafile)



if __name__ == "__main__":
    main()
