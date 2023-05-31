# HeartAttackDataAnalysis
This project, authored by Patrick O'Malley, is dedicated to analyzing data about heart attacks using Pandas and Matplotlib libraries in Python. The data is read from a CSV file, and the script produces various visualizations showing different statistics related to heart attacks.

# How to Run the Project
Make sure Python 3.x is installed on your machine. If not, download and install it from here.
Install necessary Python libraries with pip:
Copy code
pip install pandas matplotlib
Clone this repository or download the Python script.
Make sure you have the correct CSV file path in the script. Modify the file_path variable if necessary.
Run main.py which contains all the function calls.
# Project Structure
The project includes several functions, each dedicated to analyzing and visualizing a different aspect of the data.

getHeartAttack(): This function calculates the percentage of heart attacks and no heart attacks in the dataset. It also creates a pie chart to visualize this ratio.

getGender(): This function calculates the percentage of heart attacks for males and females in the dataset. A pie chart is produced to show the ratio of heart attacks between genders.

getChestPain(): This function calculates and plots the percentage of heart attacks for each chest pain type, and the percentage of pain type for all cases. Bar graphs are used for this visualization.

getBloodSugar(): This function calculates the percentage of heart attacks for people with high and regular blood sugar levels. The results are visualized with a bar chart.

getEKG(): This function calculates the percentage of heart attacks based on three different types of EKG results. The results are visualized with a bar chart.

getExercise(): This function calculates the percentage of heart attacks for people who exercised and those who did not. A bar chart is used for visualization.

Each function prints the calculated percentages and saves the generated plots to PNG images: 'HeartAttack.png', 'Gender.png', 'ChestPain.png', 'ChestPainHeartAttack.png', 'BloodSugar.png', 'EKG.png', and 'Exercise.png'.

# Data Format
The script expects the data in a specific format in a CSV file. Each row corresponds to a single patient's data, with the following columns:

attack: 1 if the patient had a heart attack, 0 otherwise
sex: 0 for male, 1 for female
cp: chest pain type (0 for typical, 1 for atypical, 2 for any pain, 3 for asymptomatic)
fbs: fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
restecg: resting electrocardiographic results (0 for normal, 1 for abnormal ST-T wave, 2 for showing probable or definite left ventricular hypertrophy)
exng: exercise induced angina (1 = yes; 0 = no)
Ensure your data adheres to this structure for the script to function correctly.

# Contributing
If you wish to contribute to this project, please make sure your changes are consistent with the current implementation. New functionalities and fixes are always welcome.
