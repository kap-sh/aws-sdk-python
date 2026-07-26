"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveredAt``."""

import datetime
from typing import TypeAlias

DiscoveredAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveredAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> DiscoveredAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
