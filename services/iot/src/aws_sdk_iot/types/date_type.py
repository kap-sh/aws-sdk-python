"""Generated from Smithy shape ``com.amazonaws.iot#DateType``."""

import datetime
from typing import TypeAlias

DateType: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateType) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> DateType:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
