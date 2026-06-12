"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpdateTimestamp``."""

import datetime
from typing import TypeAlias

UpdateTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> UpdateTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
