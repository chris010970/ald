@echo off
set GCS_BUCKET=gs://eo-ald-update
set REPO=ald

gsutil cp %GCS_BUCKET%/%REPO%/cement/plant-type/data/chips.zip .
