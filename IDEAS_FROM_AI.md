6. __ IDEAS FROM AI__
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
