from prefect import flow, task

@task
def extract():
    return "Data Extracted"

@task
def transform(data):
    import time
    time.sleep(300) # Simulates long task
    return f"{data} → Transformed"

@task
def load(data):
    raise Exception("Simulated failure")

@flow
def etl_flow(job_name: str = "Default Job"):
    raw = extract()
    processed = transform(raw)
    load(f"{job_name}: {processed}")
