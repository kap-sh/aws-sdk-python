"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#QueuedAt``."""

import datetime
from typing import TypeAlias

QueuedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: QueuedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> QueuedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
