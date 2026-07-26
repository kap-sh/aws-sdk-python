"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ExpiryTime``."""

import datetime
from typing import TypeAlias

ExpiryTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ExpiryTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> ExpiryTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
