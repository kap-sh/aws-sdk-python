"""Generated from Smithy shape ``com.amazonaws.customerprofiles#timestamp``."""

import datetime
from typing import TypeAlias

timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: timestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
