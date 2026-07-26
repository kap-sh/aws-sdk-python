"""Generated from Smithy shape ``com.amazonaws.mwaa#UpdateCreatedAt``."""

import datetime
from typing import TypeAlias

UpdateCreatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCreatedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> UpdateCreatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
