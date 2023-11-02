import requests
from prefect import flow


@flow(retries=10, log_prints=True)
def sometimes_fails():
    status = requests.get("https://httpstat.us/Random/200,500", verify=False)
    if status.status_code >= 400:
        raise Exception()
    print(status.text)


if __name__ == "__main__":
    sometimes_fails.serve(name="sometimes-fails")
