"""Generated from Smithy shape ``com.amazonaws.arczonalshift#StartTime``."""

import datetime
from typing import TypeAlias

StartTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> StartTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
