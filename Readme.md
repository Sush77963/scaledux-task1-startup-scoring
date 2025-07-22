# 🧠 Startup Scoring Engine – ScaleDux Internship Task 1

Hi! I’m Sushant Yadav, and this is my submission for the ScaleDux AI Internship (Task 1).

The goal was to build a scoring system for fictional startups based on their team strength, market size, user base, burn rate, and other metrics — sort of like a credit score but for startups.

---

## ⚙️ What This Project Does

- Reads a dataset of 100 startups (`Startup_Scoring_Dataset.csv`)
- Normalizes the key numeric fields using Min-Max scaling
- Calculates a final score out of 100 using a custom weighted formula
- Ranks startups from best to worst based on the score
- Generates charts like:
  - Score distribution
  - Feature correlation heatmap
  - Bar plot of startup scores

---

## 📊 Features I Used for Scoring

| Feature               | Why It's Important                  | Weight |
|----------------------|-------------------------------------|--------|
| Team Experience       | Good teams execute well             | 15%    |
| Market Size           | Bigger markets = more opportunity   | 20%    |
| Monthly Users         | More users = real traction          | 25%    |
| Funds Raised          | Shows external trust and runway     | 15%    |
| Valuation             | Perceived market value              | 15%    |
| Burn Rate (Inverted)  | Lower burn = more efficient         | 10%    |

Burn rate was **inverted** because higher expenses are bad for a startup.

---

## 🔍 What I Found Interesting

- Some startups with high valuations had **almost no active users** — which surprised me.
- User count and market size had the **strongest impact** on final scores.
- Burn rate was a major reason for a few good-looking startups ending up in the bottom.

---

## 📂 Output Files

Inside the `outputs/` folder, I’ve saved:

- `bar_chart.png` – All startup scores in a bar graph
- `heatmap.png` – Correlation between features
- `histogram.png` – Distribution of final scores
- `top_10_startups.csv` – Top 10 startups by score
- `bottom_10_startups.csv` – Bottom 10 startups by score

---

## 🧰 Tech Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

---

## 🏁 How to Run It

1. Install the libraries:
   pip install -r requirements.txt
2.Run the Scripts
    python startup_scoring.py
