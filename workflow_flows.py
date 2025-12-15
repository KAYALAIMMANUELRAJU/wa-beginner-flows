from prefect import flow, task

@task
def extract():
    return "Data Extracted"

@task
def transform(data):
    return f"{data} → Transformed"

@task
def load(data):
    return f"{data}"  # Logs will not show in Cloud

@task
def validate(data):
    return f"{data} → Validated"


@flow
def etl_flow(job_name: str = "Daily ETL"):
    processed = transform(raw)
    validated = validate(processed)
    load(validated)


@flow
def post_etl_flow():
    return "Post ETL tasks executed"  # Logs not visible

@flow
def notification_flow():
    return "Notification sent"  # Logs not visible
