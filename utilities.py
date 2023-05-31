#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:10:17 2023

@author: patrickomalley
"""
import pandas as pd
import matplotlib.pyplot as plt

file_path = "/users/patrickomalley/downloads/assignment3/heart.csv"
df = pd.read_csv(file_path)

def getHeartAttack():
    """
    Calculates the percentage of heart attacks and no heart attacks in the dataset. Plots a pie chart to visualize the 
    ratio of heart attacks to no heart attacks in the data.
    """
    heart_attack_count = len(df[df['attack'] == 1])
    no_heart_attack_count = len(df[df['attack'] == 0])
    total_count = len(df)

    percent_no_heart_attack = (no_heart_attack_count / total_count) * 100
    percent_heart_attack = (heart_attack_count / total_count) * 100

    print(f"The percent of no heart attacks in the data: {percent_no_heart_attack:.2f}%")
    print(f"The percent of heart attacks in the data: {percent_heart_attack:.2f}%")
    print()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie([heart_attack_count, no_heart_attack_count], labels=['Heart Attack', 'No Heart Attack'],
           autopct='%1.2f%%', startangle=90)
    ax.axis('equal') 
    plt.title('Heart Attack Ratio in Data')
    plt.savefig('HeartAttack.png')
    plt.show()

def getGender():
    """
    Calculates the percentage of heart attacks for males and females in the dataset. Plots a pie chart to visualize the
    ratio of heart attacks between males and females.
    """
    male_count = len(df[(df['sex'] == 0) & (df['attack'] == 1)])
    female_count = len(df[(df['sex'] == 1) & (df['attack'] == 1)])
    heart_attack_count = len(df[df['attack'] == 1])

    percent_male_heart_attack = (male_count / heart_attack_count) * 100
    percent_female_heart_attack = (female_count / heart_attack_count) * 100

    print(f"Male heart attacks: {percent_male_heart_attack:.2f}%")
    print(f"Female heart attacks: {percent_female_heart_attack:.2f}%")
    print()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie([percent_male_heart_attack, percent_female_heart_attack], labels=['Male', 'Female'],
           autopct='%1.2f%%', startangle=90)
    ax.axis('equal') 
    plt.title('Heart Attack Ratio between Male & Female')
    plt.savefig('Gender.png')
    plt.show()

def getChestPain():
    """
    Calculates and plots the percentage of heart attacks for each chest pain type and the percentage 
    of pain type for all cases. Displays bar graphs for both sets of data.
    """
    cp_types = {0: 'Typical', 1: 'Atypical', 2: 'Any Pain', 3: 'Asymptomatic'}

    heart_attack_by_cp = df.groupby('cp')['attack'].mean() * 100
    heart_attack_counts = df.groupby('cp')['attack'].sum()
    total_pain_counts = df['cp'].count()
    pain_reported_with_attack = heart_attack_counts / total_pain_counts * 100

    print("Chest Pain Type:")
    print("0 - typical chest pain")
    print("1 - atypical chest pain")
    print("2 - any pain that is not chest pain")
    print("3 - asymptomatic")
    for cp, percentage in heart_attack_by_cp.items():
        print(f"Chest Pain type {cp} had this percent of heart attack: {percentage:.2f}%")
    print()
    pain_counts = df['cp'].value_counts()
    total_pain_counts = pain_counts.sum()

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(cp_types.values(), pain_reported_with_attack, color='darkblue') 
    ax.set_title('Percent Pain Reported')
    ax.set_xlabel('Pain Type')
    ax.set_ylabel('Percentage Pain Type')
    plt.savefig('ChestPain.png')
    plt.show()

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(cp_types.values(), heart_attack_by_cp, color='maroon')
    ax.set_title('Percent Heart Attack by Pain Type')
    ax.set_xlabel('Pain Type')
    ax.set_ylabel('Percent Heartattack')
    plt.savefig('ChestPainHeartAttack.png')
    plt.show()


def getBloodSugar():
    high_fbs_df = df.loc[df['fbs'] == 1]
    reg_fbs_df = df.loc[df['fbs'] == 0]
    
    high_fbs_attack = round((high_fbs_df['attack'].sum() / high_fbs_df.shape[0]) * 100, 2)
    reg_fbs_attack = round((reg_fbs_df['attack'].sum() / reg_fbs_df.shape[0]) * 100, 2)
    print(f"High blood sugar heart attack percentage: {high_fbs_attack}%")
    print(f"Regular blood sugar heart attack percentage: {reg_fbs_attack}%")
    print()
    fbs_attack_data = {'High': high_fbs_attack, 'Regular': reg_fbs_attack}
    fig, ax = plt.subplots()
    ax.bar(fbs_attack_data.keys(), fbs_attack_data.values(), color = 'green')
    ax.set_title('Percent Heart Attack by Blood Sugar Level')
    ax.set_xlabel('Blood Sugar')
    ax.set_ylabel('Percent Heartattack')
    plt.savefig('BloodSugar.png')
    plt.show()

def getEKG():
    """
    Calculates the percentage of heart attacks for people with high and regular blood sugar levels in the dataset. 
    Plots a bar chart to visualize the relationship between blood sugar levels and heart attack occurrences.
    """
    ekg_types = ['Normal', 'Abnormal ST-T Wave EKG Type', 'Abnormal Left Ventricular']
    print("EKG type:")
    print("0 - EKG was normal")
    print("1 - EKG had an abnormality with ST-T Wave")
    print("2 - EKG had an abnormality in the Left ventricular")
    ekg_data = []
    for i in range(3):
        ekg_heart_attacks = df[df['restecg'] == i]['attack'].sum()
        ekg_total = len(df[df['restecg'] == i])
        ekg_rate = ekg_heart_attacks / ekg_total * 100
        ekg_data.append(ekg_rate)
        print(f'Resting EKG Type {i} had this percent of heart attack: {ekg_rate:.2f}%')
    
    plt.bar(ekg_types, ekg_data, color = 'red')
    plt.title('Percent Heart Attack Resting EKG')
    plt.xlabel('EKG Type')
    plt.ylabel('Percent')
    plt.xticks(fontsize=7)
    plt.savefig('EKG.png')
    plt.show()
    print()
    
def getExercise():
    """
    Calculates the percentage of heart attacks for people who exercised and those who did not in the dataset. 
    Plots a bar chart to visualize the relationship between exercise and heart attack occurrences.
    """

    exercise_attacks = df[df["exng"] == 1]["attack"].value_counts(normalize=True) * 100
    no_exercise_attacks = df[df["exng"] == 0]["attack"].value_counts(normalize=True) * 100
    
    fig, ax = plt.subplots()
    ax.bar(["Yes", "No"], [exercise_attacks[1], no_exercise_attacks[1]], color = 'purple')
    ax.set_ylabel("Percent Heart Attack")
    ax.set_xlabel("Exercise")
    ax.set_title("Percent Heart Attack if Exercising")
    plt.savefig('Exercise.png')
    plt.show()

    print(f"Percent who Exercised and had heart attack: {exercise_attacks[1]:.2f}%")
    print(f"Percent with No Exercise and had heart attack: {no_exercise_attacks[1]:.2f}%")