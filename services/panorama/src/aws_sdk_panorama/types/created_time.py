"""Generated from Smithy shape ``com.amazonaws.panorama#CreatedTime``."""

import datetime
from typing import TypeAlias

CreatedTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreatedTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CreatedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
