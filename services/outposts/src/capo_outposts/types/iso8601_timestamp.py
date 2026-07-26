"""Generated from Smithy shape ``com.amazonaws.outposts#ISO8601Timestamp``."""

import datetime
from typing import TypeAlias

ISO8601Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ISO8601Timestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> ISO8601Timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
