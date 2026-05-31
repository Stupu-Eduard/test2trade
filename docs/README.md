# Project Title and Description
# Test2Trade
Web platform for backtesting trading strategies. Upload Python strategies, run them on real market data, and analyze results through an interactive dashboard. Features AI-assisted strategy generation from natural language rules.



# Project Information

### Programming languages used:

* Backend of the Web Server → Spring Boot
* Frontend of the Web Server → React
* Testing the strategy → Python
* Database Configuration → PostgreSQL

### Frontend Ideas:

1. At the start you introduce your trading strategy in Python code
2. After that you choose on what data you want the strategy to be tested in (Binance, Yahoo Finance,other)
3. After introducing the Python code, it will begin the backtest
4. At the end it will bring a visual dashboard with every useful information for the trader:
    * The winrate
    * Lowest Drawdown
    * Monday-Friday chart with info on how that day was as average (for the traders to see when not to trade)
    * If it is possible to get information about high impact news and to make a check if they are willing to backtest while there are high impact news in that day or not.
5. Maybe implement the different types of backtesting with different intervals (__I need more research on this__).
6. After everything else is implemented, starting the research on how to implement a custom AI that will transform your trading idea in a:
    * High quality checklist rules first (making it close to being highly implementable as Python code)
    * And if the customer accepts that checklist, the AI to transform that checklist into Python code

## 3. System Architecture

### 3.1. Use Case Diagram
![Use Case Diagram](images/use_case_diagram.svg)

<br>

### 3.2. Component Architecture
![architecture_diagram](images/architecture_diagram.svg)

<br>

### 3.2. Entity-Relationship Diagram
![entity_relationship_diagram](images/entity_relationship_diagram.svg)

<br>

### 3.3. Sequence Diagram
![sequence_diagram](images/sequence_diagram.svg)