<div align="center">
  <h1>📈 Test2Trade</h1>
  <p><i>Web platform for backtesting trading strategies.</i></p>
  
  <p>
    <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white" alt="Spring Boot" />
    <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  </p>
</div>

> **⚠️ DEVELOPMENT STATUS:** This project is in **very early development**. I am currently in the ideation and architectural design phase. All features and functionalities listed below are planned ideas and concepts, not yet implemented.

---

## 📖 About The Project

Upload Python strategies, run them on real market data, and analyze results through an interactive dashboard. Test2Trade bridges the gap between raw code and actionable market insights, featuring AI-assisted strategy generation from natural language rules.

## ✨ Proposed Features & User Flow

1. **Strategy Definition:** Introduce your custom trading strategy directly via **Python** code.
2. **Data Selection:** Choose the historical market data source you want to test against (e.g., *Binance, Yahoo Finance*).
3. **Execution Engine:** Trigger the backtesting process to simulate trades over the selected data.
4. **Interactive Visual Dashboard:** Analyze comprehensive trading metrics, including:
   * 🏆 **Winrate** & 📉 **Lowest Drawdown**
   * 📊 **Day-by-Day Analysis:** Monday-Friday average charts to identify optimal trading days.
   * 📰 **News Filter:** Overlay high-impact market news to test strategy resilience during volatility.
5. **Advanced Intervals:** *(In Research)* Support for diverse backtesting intervals and timeframes.
6. **🤖 AI Strategy Assistant:** *(Upcoming)* Transform trading ideas into executable code:
   * Generates a high-quality rules checklist from natural language inputs.
   * Converts user-approved checklists directly into deployable Python strategy code.

---

## 🏗️ System Architecture

### 3.1. Use Case Diagram
![Use Case Diagram](images/use_case_diagram.svg)

<br>

### 3.2. Component Architecture
![architecture_diagram](images/architecture_diagram.svg)

<br>

### 3.3. Entity-Relationship Diagram
![entity_relationship_diagram](images/entity_relationship_diagram.svg)

<br>

### 3.4. Sequence Diagram
![sequence_diagram](images/sequence_diagram.svg)
