"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#LastUpdatedAt``."""

import datetime
from typing import TypeAlias

LastUpdatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> LastUpdatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
