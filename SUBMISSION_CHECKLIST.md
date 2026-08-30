# FORESIGHT — Internship Submission Checklist

**Prepared by: Vivek**

## Core project
- [x] Reproducible data pipeline
- [x] Data quality / EDA report
- [x] Weekly SKU demand forecasting
- [x] Seasonal-naive baseline
- [x] Rolling-origin backtesting
- [x] WAPE evaluation
- [x] Inventory risk scoring
- [x] Recommended actions
- [x] Streamlit dashboard
- [x] FastAPI scoring service
- [x] README and requirements

## Before final submission
- [ ] Install requirements and run `python run_pipeline.py`
- [ ] Run `streamlit run app/app.py` and test the dashboard
- [ ] Run the API and test `/health` and `/score`
- [ ] Push repository to GitHub
- [ ] Deploy dashboard and scoring service
- [ ] Record 3–5 minute demo
- [ ] Put live URLs into the submission form

## Data-source disclosure
The source is a Kaggle retail inventory dataset. The Zidio brief specifies four simulated extracts; this source is a single retail table. The project documents the mapping and does not fabricate unavailable fields such as unit cost, lead time, or reorder point.
