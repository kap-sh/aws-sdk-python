"""Generated from Smithy shape ``com.amazonaws.networkmonitor#Iso8601Timestamp``."""

import datetime
from typing import TypeAlias

Iso8601Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Iso8601Timestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> Iso8601Timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
