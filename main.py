import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Define Input and Output Variables
waiting_time = ctrl.Antecedent(np.arange(0, 61, 1), 'waiting_time')
food_quality = ctrl.Antecedent(np.arange(1, 11, 1), 'food_quality')
service_rating = ctrl.Consequent(np.arange(0, 101, 1), 'service_rating')

# 2. Define Fuzzy Sets
# Waiting Time
waiting_time['short'] = fuzz.trapmf(waiting_time.universe, [0, 0, 5, 15])
waiting_time['moderate'] = fuzz.trimf(waiting_time.universe, [10, 25, 40])
waiting_time['long'] = fuzz.trapmf(waiting_time.universe, [35, 50, 60, 60])

# Food Quality
food_quality['bad'] = fuzz.trapmf(food_quality.universe, [1, 1, 3, 5])
food_quality['average'] = fuzz.trimf(food_quality.universe, [4, 6, 8])
food_quality['good'] = fuzz.trapmf(food_quality.universe, [7, 9, 10, 10])

# Service Rating
service_rating['low'] = fuzz.trapmf(service_rating.universe, [0, 0, 30, 50])
service_rating['medium'] = fuzz.trimf(service_rating.universe, [40, 60, 80])
service_rating['high'] = fuzz.trapmf(service_rating.universe, [70, 90, 100, 100])

# Display the membership function plots
waiting_time.view()
food_quality.view()
service_rating.view()

# 3. Define Fuzzy Rules
# The rules connect the inputs to the output based on a logical structure.
rule1 = ctrl.Rule(waiting_time['short'] & food_quality['good'], service_rating['high'])
rule2 = ctrl.Rule(waiting_time['short'] & food_quality['average'], service_rating['high'])
rule3 = ctrl.Rule(waiting_time['short'] & food_quality['bad'], service_rating['medium'])
rule4 = ctrl.Rule(waiting_time['moderate'] & food_quality['good'], service_rating['high'])
rule5 = ctrl.Rule(waiting_time['moderate'] & food_quality['average'], service_rating['medium'])
rule6 = ctrl.Rule(waiting_time['moderate'] & food_quality['bad'], service_rating['low'])
rule7 = ctrl.Rule(waiting_time['long'] & food_quality['good'], service_rating['medium'])
rule8 = ctrl.Rule(waiting_time['long'] & food_quality['average'], service_rating['low'])
rule9 = ctrl.Rule(waiting_time['long'] & food_quality['bad'], service_rating['low'])

# 4. Build the Fuzzy Control System
fuzzy_control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
fuzzy_simulator = ctrl.ControlSystemSimulation(fuzzy_control_system)

# 5. Function for Testing
def test_fuzzy_system(wait_time, food_quality_val):
    fuzzy_simulator.input['waiting_time'] = wait_time
    fuzzy_simulator.input['food_quality'] = food_quality_val
    fuzzy_simulator.compute()
    rating = fuzzy_simulator.output['service_rating']
    return rating

# Test with 10 different data points
test_data = [
    (10, 9), (25, 7.5), (5, 5), (45, 8), (30, 6),
    (55, 3), (1, 10), (20, 4), (40, 7), (15, 6.5)
]

print("Test Results Table:")
print("{:<15} {:<15} {:<15}".format("Waiting Time", "Food Quality", "Service Rating"))
print("-" * 45)
for wait, quality in test_data:
    result = test_fuzzy_system(wait, quality)
    print(f"{wait:<15} {quality:<15} {result:<15.2f}")

# Display the output for a specific case visually
fuzzy_simulator.input['waiting_time'] = 25
fuzzy_simulator.input['food_quality'] = 7.5
fuzzy_simulator.compute()
print(f"\nRating for a Waiting Time of 25 and Food Quality of 7.5: {fuzzy_simulator.output['service_rating']:.2f}")
service_rating.view(sim=fuzzy_simulator)
plt.show()