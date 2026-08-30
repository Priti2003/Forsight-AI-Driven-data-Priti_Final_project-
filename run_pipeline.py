from src.pipeline import run_pipeline
from src.forecast import train_and_backtest

if __name__ == "__main__":
    run_pipeline()
    results = train_and_backtest()
    print("\nBacktest results:")
    print(results.to_string(index=False))
    print("\nPipeline complete.")
