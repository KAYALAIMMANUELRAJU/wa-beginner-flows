from prefect import flow

@flow
def post_etl_flow():
    return "Post ETL tasks executed"  # output won't appear in Cloud logs for push-based runs
