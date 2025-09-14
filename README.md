"Implementations of supervised and reinforcement learning projects (k-NN for shopping predictions, Q-learning for Nim game) from CS50AI[https://cs50.harvard.edu/ai/projects/4/]." 

📌 Projects
1. 🛒 Shopping – Predicting Purchasing Intent

Goal: Predict whether a user visiting an online shopping website will complete a purchase.

Method: Implement a k-Nearest Neighbor (k-NN) classifier using scikit-learn.

Dataset: About 12,000 user sessions with features like page views, bounce rates, browser type, weekend/weekday, etc.

Output: The model predicts whether the session ends in a purchase (Revenue = TRUE/FALSE).

Evaluation:

Sensitivity (True Positive Rate) – how many actual purchasers are correctly identified.

Specificity (True Negative Rate) – how many non-purchasers are correctly identified.

📂 Folder: shopping/

shopping.py: main code to load data, train model, and evaluate.

shopping.csv: dataset (not included here, available in CS50 distribution).


2. 🎮 Nim AI – Reinforcement Learning with Q-Learning

Goal: Build an AI that learns to play the game Nim through reinforcement learning.

Method: Implement Q-learning to assign rewards to state-action pairs.

Mechanics:

State = configuration of piles.

Action = removing some objects from a pile.

AI trains by playing against itself and improves over time.

Core Functions to Implement:

get_q_value

update_q_value

best_future_reward

choose_action

📂 Folder: nim/

nim.py: defines game mechanics and AI learning.

play.py: lets a human play against the trained AI.


🚀 Getting Started
Prerequisites

Python 3

scikit-learn (pip install scikit-learn)