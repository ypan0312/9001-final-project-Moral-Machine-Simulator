from datetime import datetime
import json
import random
import os
from collections import defaultdict
from socket import gethostbyname, gethostname

class Scenario:
    """
    Represents a single moral dilemma scenario.
    Contains an ID, scenario text, and two choices (each with a description and ethical label).
    """
    def __init__(self, sid: str, scenario: str, choices: dict):
        self.sid = sid
        self.scenario = scenario
        self.choices = choices

    def display(self):
        """Prints the scenario and its choices to the console."""
        print(f"{self.scenario}")
        for key, value in self.choices.items():
            print(f"{key}. {value['description']}")

class Simulator:
    """
    Core class managing the moral machine simulation process.
    Loads scenarios, runs the interaction loop, logs decisions, and summarizes results.
    """
    def __init__(self, scenario_file: str, ethics_file: str, lang: str):
        self.scenario_file = "scenarios_cn.json" if lang == "cn" else "scenarios.json"
        self.ethics_file = ethics_file
        self.lang = lang
        self.scenarios: list[Scenario] = []
        self.ethics_explanations = {}
        self.user_ip = gethostbyname(gethostname())
        self.decision_log = {}

    def load_scenarios(self):
        """Loads and shuffles scenarios from a JSON file."""
        try:
            with open(self.scenario_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                random.shuffle(data)
                self.scenarios = [Scenario(d["id"], d["scenario"], d["choices"]) for d in data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading scenarios: {e}")
            self.scenarios = []

    def load_ethics_explanations(self):
        """Load ethics explanations from external dictionary file based on language."""
        try:
            with open(self.ethics_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.ethics_explanations = {k: v.get(self.lang, "") for k, v in data.items()}
        except Exception as e:
            print(f"Failed to load ethics explanations: {e}")
            self.ethics_explanations = {}

    def run(self):
        """Run the main decision-making simulation loop."""
        print(f"Your IP address: {self.user_ip}\n")
        for i, scenario in enumerate(self.scenarios, 1):
            print(f"Scenario {i}:")
            scenario.display()
            user_choice = ""
            while user_choice not in scenario.choices:
                user_choice = input("Your decision (A/B): ").strip().upper()
            ethics = scenario.choices[user_choice]["ethics"]
            print(f"\nEthical Framework: {ethics}")
            print("Explanation:", self.ethics_explanations.get(ethics, "No explanation available."), "\n")
            self.decision_log[scenario.sid] = ethics

    def summarize_results(self):
        """Count and print how many times each ethical framework was chosen."""
        summary = defaultdict(int)
        for ethics in self.decision_log.values():
            summary[ethics] += 1
        print("Summary of your ethical leanings:")
        for k, v in summary.items():
            print(f"- {k}: {v} times")
        if summary:
            top_ethics = max(summary, key=summary.get)
            print(f"\nYou tend to lean toward: {top_ethics}\n")
        return summary

    def save_log(self, log_file="decision_log.json"):
        """Save the user's choices and summary to a log file (grouped by IP)."""
        if os.path.exists(log_file):
            with open(log_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {}
        data[self.user_ip] = {
            "decisions": self.decision_log,
            "summary": dict(self.summarize_results()),
            "timestamp": datetime.now().isoformat()
        }
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def add_custom_scenario(self):
        """Allow the user to add a new scenario to the dataset."""
        print("\nAdd Your Own Moral Dilemma:")
        try:
            scenario_text = input("Describe the scenario:\n")
            choice_a = input("Describe option A:\n")
            ethics_a = input("Ethical framework for A (Utilitarianism / Deontology / Virtue Ethics):\n")
            choice_b = input("Describe option B:\n")
            ethics_b = input("Ethical framework for B (Utilitarianism / Deontology / Virtue Ethics):\n")
            new_scenario = {
                "id": f"custom_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                "scenario": scenario_text,
                "choices": {
                    "A": {"description": choice_a, "ethics": ethics_a},
                    "B": {"description": choice_b, "ethics": ethics_b}
                }
            }
            with open(self.scenario_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []

        data.append(new_scenario)
        with open(self.scenario_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Your scenario has been added!\n")

# Unit test to ensure ethics explanation integrity
def test_ethics_explanation():
    sim = Simulator(scenario_file, "ethics_dictionary.json", lang)
    sim.load_ethics_explanations()
    assert sim.ethics_explanations["Utilitarianism"].startswith("Utilitarianism promotes")
    assert "Deontology" in sim.ethics_explanations
    assert isinstance(sim.ethics_explanations["Virtue Ethics"], str)
    print("All ethics explanation tests passed.")

# Entry point
if __name__ == "__main__":
    test_ethics_explanation()
    print("Welcome to the Moral Machine Simulator.")
    print("This is an anonymous test. Your IP address and decisions will be recorded.")
    print("You may quit at any time by pressing Ctrl+C.\n")

    lang = input("Please choose a language / 请选择语言 (en/cn): ").strip().lower()

    # 根据语言选择对应的场景文件
    scenario_file = "scenarios_cn.json" if lang == "cn" else "scenarios.json"
    sim = Simulator(scenario_file, "ethics_dictionary.json", lang)
    sim.load_scenarios()
    sim.load_ethics_explanations()
    if not sim.scenarios:
        exit()
    sim.run()
    sim.save_log()
    if input("Would you like to add your own dilemma? (y/n): ").strip().lower() == "y":
        sim.add_custom_scenario()
