6. __IDEAS FROM AI__
    * Code Audit: Overfitting and Lookahead Bias Detection
        
        The biggest pitfall in backtesting is a strategy that looks flawless on historical data but fails completely in live markets. The AI can scan the uploaded Python script to detect if the strategy is "peeking" into future data (lookahead bias) or if its parameters are hyper-specific and over-optimized strictly for the tested history (overfitting).
    * Contextual Analysis and Narrative Report Generation
       
        Instead of just providing a dashboard with cold numbers (win rate, drawdown), you can send the raw backtest results to an LLM to generate a human-readable summary.
      
       AI-Generated Example: "Your strategy shows a solid win rate, but I noticed it suffers major losses during price consolidation phases on volatile instruments like the Nasdaq 100 or XAUUSD. Additionally, the majority of losing trades occur within the first 30 minutes of the New York session open."
    * Parameter Optimization (AI as a Trading Co-Pilot)
      
      If a backtest ends in the negative, the AI can analyze the performance metrics and proactively suggest code improvements. It could run slightly modified variations of the strategy in the background and present a proposal for adjusting the Stop Loss or Take Profit levels based on historical volatility.
    
    * For each candle/day in the backtest:
      1. Check if there's a HIGH IMPACT event on that day
         (for the respective currency — e.g., USD for XAUUSD)
      2. If the user has checked "skip news days" → skip the trade
      3. If they've checked "trade anyway" → execute it normally
      4. (Optional) If they've checked "extended window" → skip X hours before and after news
    * Store the historical CSV files locally on the server or within an optimized PostgreSQL database. Consequently, when a user initiates a backtest for a specific dataset—such as 'BTC/USDT 1m for the year 2023'—the engine retrieves the pristine, localized dataset instead of relying on potentially unstable, on-the-fly API requests to external providers like Yahoo Finance.

### Possible Setbacks:


   1. Python Execution is a Serious Security Problem
     User uploads arbitrary code that runs on your server. You need serious sandboxing
     (Docker containers per execution, resource limits, timeouts). If you don't solve this,
     you can't publish a real platform.


   2. Market Data = Costs or Limitations
      Yahoo Finance has rate limits. Binance API is okay for crypto. If you want forex data
      (XAUUSD, which you yourself trade), you need separate sources — and data quality makes
      or breaks a backtest.


   3. Realistic Backtesting is Hard to Implement Correctly
      Slippage, spread, commissions, look-ahead bias — if you don't model them, the results
      are useless or misleading for users.
      Data Integrity and Granularity


   4. While platforms such as Yahoo Finance provide reliable historical data for macro timeframes (e.g., daily or weekly intervals), free-tier APIs frequently exhibit data fragmentation on lower intraday intervals (such as 1m, 5m, or 15m). These inconsistencies—often manifesting as missing candlesticks or inaccurate volume metrics—can severely compromise the validity of the testing process. High-fidelity backtesting inherently demands immaculate, high-resolution historical datasets to ensure accurate performance metrics.
      Asynchronous Execution and Concurrency


   5. Executing a comprehensive backtest over extended periods (e.g., five years of minute-by-minute historical data) is a computationally intensive operation that introduces significant latency. To prevent thread blocking and ensure an optimal user experience, the Spring Boot backend must delegate the execution workload to the Python engine asynchronously. Consequently, the React frontend should implement a non-blocking user interface, utilizing real-time communication protocols (such as WebSockets) to receive server-sent events and seamlessly notify the user upon the successful completion of the computational task.