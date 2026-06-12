"""Generated from Smithy shape ``com.amazonaws.scheduler#LastModificationDate``."""

import datetime
from typing import TypeAlias

LastModificationDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastModificationDate) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> LastModificationDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
