"""Generated from Smithy shape ``com.amazonaws.opensearch#StartAt``."""

import datetime
from typing import TypeAlias

StartAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> StartAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
