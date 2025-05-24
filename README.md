# 9001-final-project-Moral-Machine-Simulator
# Moral Machine Simulator

An interactive Python program that simulates ethical dilemmas inspired by MIT's Moral Machine project.

---

## Project Overview

This command-line simulator presents users with a series of moral dilemmas — such as self-driving car choices — and asks them to choose between two ethically challenging options. Each decision is linked to a core ethical theory (e.g., Utilitarianism, Deontology, Virtue Ethics).

The program tracks user choices, explains the ethical basis, and saves decisions along with the user's IP (anonymized) for statistical analysis.

---

## File Structure

AI Ethics: The Moral Dilemma Game/
│
├── moral_machine.py # Main program script (with class-based design)
├── scenarios.json # English version of 6 built-in moral dilemmas
├── scenarios_cn.json # Chinese version of the same dilemmas
├── ethics_dictionary.json # Core ethical theory explanations in EN/CN
├── decision_log.json # Auto-generated: stores user logs by IP

---

## Target Audience

Students, educators, or the general public interested in AI ethics, philosophy of technology, or interactive decision-making simulations.