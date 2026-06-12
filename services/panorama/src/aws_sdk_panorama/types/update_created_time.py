"""Generated from Smithy shape ``com.amazonaws.panorama#UpdateCreatedTime``."""

import datetime
from typing import TypeAlias

UpdateCreatedTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCreatedTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> UpdateCreatedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
