"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveryFinishedAt``."""

import datetime
from typing import TypeAlias

DiscoveryFinishedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveryFinishedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> DiscoveryFinishedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
