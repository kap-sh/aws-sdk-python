"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#LastModifiedTimestamp``."""

import datetime
from typing import TypeAlias

LastModifiedTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastModifiedTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> LastModifiedTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
