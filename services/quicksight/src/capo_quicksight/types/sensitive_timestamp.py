"""Generated from Smithy shape ``com.amazonaws.quicksight#SensitiveTimestamp``."""

import datetime
from typing import TypeAlias

SensitiveTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> SensitiveTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
