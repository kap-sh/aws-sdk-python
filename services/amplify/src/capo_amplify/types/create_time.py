"""Generated from Smithy shape ``com.amazonaws.amplify#CreateTime``."""

import datetime
from typing import TypeAlias

CreateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreateTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CreateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
