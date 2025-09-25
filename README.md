
# 🍽️ Fuzzy Logic Restaurant Service Rating System

This project implements an Expert System based on Fuzzy Logic to evaluate the quality of a restaurant's service. The system takes two inputs, Waiting Time and Food Quality, to generate a nuanced and accurate Service Rating.
## ✨ Key Features

 - Intelligent Assessment: Uses fuzzy logic to handle the ambiguity and uncertainty inherent in human-like judgments.
- Clear Visualization: Displays membership function graphs and defuzzification results for better understanding.
- Highly Customizable: Easily adaptable by modifying fuzzy rules or membership function parameters to suit different needs.


## 🚀 Getting Started

Ensure you have Python 3.x installed. Then, install the required packages using  ``` pip ```.

#### Dependencies:
This project requires the following libraries:

- ``` numpy ```
- ``` scikit-fuzzy ```
- ``` matplotlib ```

To install them, run the following command in your terminal:
    
``` bash
  pip install numpy scikit-fuzzy matplotlib
```
## ⚙️ How to Run

#### Execute the Program

Open your terminal or command prompt, navigate to the directory where your project file (e.g., ``` main.py ```) is located, and run the following command:

```bash
python main.py
```

#### Understanding the Output

The program will output several key components:

1. Membership Function Plots: Three separate plots will appear, showing the fuzzy sets for Waiting Time, Food Quality, and Service Rating.

2. Test Results Table: A table will be printed in the terminal, displaying the rating outcomes for 10 different scenarios.

3. Simulation Plot: An interactive plot will show how the fuzzy system processes the inputs of ``` Waiting Time: 25 ``` and ``` Food Quality: 7.5 ``` to arrive at the final rating. The vertical blue line represents the final defuzzified output.

## 💡 How It Works

The system follows a standard four-step fuzzy inference process:

1. Fuzzification: Converts crisp input values (e.g., a waiting time of 25 minutes) into a degree of membership in fuzzy sets (e.g., ```moderate``` with a degree of 1.0).

2. Rule Evaluation: The system evaluates ```IF-THEN``` rules (e.g., ```IF Waiting Time is MODERATE AND Food Quality is GOOD THEN Rating is HIGH```) using the ```min()``` operator.

3. Aggregation: The results from all active rules are combined into a single output fuzzy set.

4. Defuzzification: The aggregated fuzzy set is converted back into a single, crisp value (a single number) using the centroid method.