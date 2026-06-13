"""Generated from Smithy shape ``com.amazonaws.inspector2#FirstSeen``."""

import datetime
from typing import TypeAlias

FirstSeen: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: FirstSeen) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> FirstSeen:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
