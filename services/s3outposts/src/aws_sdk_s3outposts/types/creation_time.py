"""Generated from Smithy shape ``com.amazonaws.s3outposts#CreationTime``."""

import datetime
from typing import TypeAlias

CreationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreationTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CreationTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
