
# Moral Machine Simulator

An interactive Python program that lets users explore ethical dilemmas faced by AI, inspired by MIT’s Moral Machine project.

---

##  Overview

How should an AI decide between two morally difficult options?  
This simulator puts you in control. As the user, you’ll navigate through multiple moral dilemmas, such as:

- Should a self-driving car hit an elderly pedestrian or swerve into a jaywalking child?
- Should a rescue robot save two adults or risk everything to rescue a trapped child?

Each choice reveals your ethical tendency — based on **Utilitarianism**, **Deontology**, or **Virtue Ethics** — and provides a brief explanation of the ethical theory behind your decision.

---

##  Features

- Randomized ethical scenarios every run  
- Language selection: English or 中文  
- Explanations of core ethics loaded from file  
- Summary of your overall ethical leanings  
- Add your own dilemma at the end  
- Decision log saved (anonymized by IP)

---

##  File Structure

```
Moral Machine Simulator/
├── moral_machine.py           # Main script (object-oriented structure)
├── scenarios.json             # English dilemmas (x6)
├── scenarios_cn.json          # 中文困境（与英文版本一致）
├── ethics_dictionary.json     # Ethics framework descriptions (EN & CN)
├── decision_log.json          # Log of past user decisions (auto-generated)
├── README.md                  # This file
```

---

## ▶️ How to Run

1. Open terminal or your Python IDE.
2. Make sure you are in the project folder.
3. Run:
   ```bash
   python moral_machine.py
   ```
4. Follow the on-screen instructions.

---

##  Target Audience

This project is for:
- Students curious about ethics and AI
- Philosophy and CS crossover learners
- Anyone who enjoys reflective thinking

---

##  Sample Output

```
Scenario 1:
A self-driving car must choose between swerving to hit a jaywalking child or staying on course and hitting an elderly pedestrian.
Your decision (A/B): B

Ethical Framework: Utilitarianism
Explanation: Utilitarianism promotes actions that maximize overall happiness or minimize harm.
```

