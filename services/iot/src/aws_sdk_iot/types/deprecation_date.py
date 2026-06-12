"""Generated from Smithy shape ``com.amazonaws.iot#DeprecationDate``."""

import datetime
from typing import TypeAlias

DeprecationDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DeprecationDate) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> DeprecationDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
