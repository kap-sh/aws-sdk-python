"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#HubConfigurationUpdatedAt``."""

import datetime
from typing import TypeAlias

HubConfigurationUpdatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: HubConfigurationUpdatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> HubConfigurationUpdatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
