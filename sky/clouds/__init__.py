"""Clouds in Sky."""
from sky.clouds.cloud import Cloud
from sky.clouds.cloud import Region
from sky.clouds.cloud import Zone
from sky.clouds.aws import AWS
from sky.clouds.azure import Azure
from sky.clouds.gcp import GCP
from sky.clouds.local import Local

__all__ = [
    'AWS',
    'Azure',
    'CLOUD_REGISTRY',
    'Cloud',
    'GCP',
    'Local',
    'Region',
    'Zone',
    'from_str',
]

CLOUD_REGISTRY = {
    'aws': AWS(),
    'gcp': GCP(),
    'azure': Azure(),
    'local': Local(),
}


def from_str(name: str) -> 'Cloud':
    return CLOUD_REGISTRY[name.lower()]
