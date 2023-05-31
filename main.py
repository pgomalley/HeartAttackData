#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:07:31 2023

@author: patrickomalley
"""

from utilities import *

def main():
    print("\033[94mHeart Attack Analysis\033[0m")
    print()
    print("These are the factors related to heart attacks that are considered in this data:")
    print("1. Heart Attack Percentage is calculated based on all data to see if the data is skewed.")
    print("2. Gender Percent is used to distinguish between the heart attack rates in men and women.")
    print("3. Four types of Chest Pain are considered, along with the associated heart attack percentages.")
    print("4. Fasting Blood Sugar levels are considered to determine possible coronary heart disease.")
    print("5. EKG is considered, as it detects heart problems that can forecast chance of future heart attacks")
    print("6. Exercise is considered to see if likelihood of heart attack increases when physically active.")
    print()
    getHeartAttack()
    getGender()
    getChestPain()
    getBloodSugar()
    getEKG() 
    getExercise()

if __name__ == "__main__":
    main()
