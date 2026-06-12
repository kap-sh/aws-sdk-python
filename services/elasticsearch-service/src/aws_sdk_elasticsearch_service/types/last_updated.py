"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#LastUpdated``."""

import datetime
from typing import TypeAlias

LastUpdated: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdated) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> LastUpdated:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
