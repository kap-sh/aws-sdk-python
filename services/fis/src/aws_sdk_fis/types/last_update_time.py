"""Generated from Smithy shape ``com.amazonaws.fis#LastUpdateTime``."""

import datetime
from typing import TypeAlias

LastUpdateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdateTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> LastUpdateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
