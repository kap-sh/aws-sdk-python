"""Generated from Smithy shape ``com.amazonaws.inspector2#DateTimeTimestamp``."""

import datetime
from typing import TypeAlias

DateTimeTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> DateTimeTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
