"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#StartedAt``."""

import datetime
from typing import TypeAlias

StartedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> StartedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
