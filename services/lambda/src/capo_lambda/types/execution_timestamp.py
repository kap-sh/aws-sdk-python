"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionTimestamp``."""

import datetime
from typing import TypeAlias

ExecutionTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionTimestamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> ExecutionTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
