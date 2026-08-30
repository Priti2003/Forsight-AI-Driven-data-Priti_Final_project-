# Project FORESIGHT — Demand & Inventory Intelligence

## Zidio Data Science Internship

**Prepared by: Vivek**

This implementation adapts the provided Kaggle **Retail Store Inventory Forecasting** dataset to the FORESIGHT engagement brief.

### Dataset
- 73,100 raw records
- 20 products
- 5 stores
- 5 categories
- Date range: 2022-01-01 to 2024-01-01
- Daily sales, inventory, orders, price, discount, promotion, competitor pricing and seasonality fields.

### Important data mapping
The Zidio brief describes four extracts (`sales_daily`, `sku_master`, `calendar`, `inventory_snapshots`). The downloaded Kaggle dataset is a single retail table, so this project does **not** pretend that unavailable fields exist. The pipeline converts the available fields into a weekly SKU-level analytical table.

### Run
```bash
pip install -r requirements.txt
python run_pipeline.py
streamlit run app/app.py
```

Scoring API:
```bash
uvicorn service.api:app --reload
```

### Model
- Weekly SKU demand
- Seasonal-naive baseline: same week one year earlier (`lag_52`)
- Lag and rolling features
- Random Forest regression
- Rolling-origin 8-week backtests
- Primary metric: WAPE
- Fixed random seed and no random train/test split

### Backtest result on the supplied dataset
Three rolling-origin folds were run before packaging:
| Fold | Model WAPE | Seasonal-naive WAPE |
|---|---:|---:|
| 1 | 8.71% | 14.34% |
| 2 | 9.10% | 16.98% |
| 3 | 19.56% | 26.22% |

The model beat the baseline in all three evaluated folds. These are dataset-derived results, not fabricated targets.

### Risk logic
- REORDER NOW: projected demand exceeds available stock with safety allowance.
- MARKDOWN / CLEAR: on-hand stock materially exceeds projected demand.
- WATCH / VOLATILE: both conditions are present.
- HEALTHY: neither condition is triggered.

### Limitations
The Kaggle data does not provide all fields requested by the original brief, notably unit cost, list price, lead time and reorder point. The packaged risk service therefore uses transparent proxy rules rather than inventing those fields.

## Suggested submission
- Git repository
- README
- Pipeline/model code
- Streamlit dashboard
- FastAPI scoring service
- EDA memo
- Executive readout
- Demo video
