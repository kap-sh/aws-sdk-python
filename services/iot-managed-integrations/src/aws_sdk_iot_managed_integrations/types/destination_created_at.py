"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DestinationCreatedAt``."""

import datetime
from typing import TypeAlias

DestinationCreatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DestinationCreatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> DestinationCreatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
