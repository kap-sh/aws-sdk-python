"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdatedAt``."""

import datetime
from typing import TypeAlias

UpdatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> UpdatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
