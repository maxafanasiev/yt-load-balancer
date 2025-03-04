from google.cloud import run_v2
from loguru import logger

from app.settings.constants import REGIONS, PROJECT_ID
from app.settings.settings import api_settings


def get_all_cloud_run_service_uris():
    client = run_v2.ServicesClient()

    flat_runs = []
    for region in REGIONS:
        parent = f"projects/{PROJECT_ID}/locations/{region}"
        services = client.list_services(parent=parent)
        flat_runs.extend(services)

    all_uris = [run.uri for run in flat_runs if api_settings.SCRAPER_SERVICE_PREFIX in run.uri]
    logger.info(f"Service count in all regions: {len(all_uris)}")
    return all_uris
