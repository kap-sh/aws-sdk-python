"""Generated from Smithy shape ``com.amazonaws.opensearch#StartTimestamp``."""

import datetime
from typing import TypeAlias

StartTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> StartTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
