"""Generated from Smithy shape ``com.amazonaws.inspector2#LastSeen``."""

import datetime
from typing import TypeAlias

LastSeen: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastSeen) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> LastSeen:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
