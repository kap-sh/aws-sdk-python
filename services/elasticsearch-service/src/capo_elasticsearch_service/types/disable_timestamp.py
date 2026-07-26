"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DisableTimestamp``."""

import datetime
from typing import TypeAlias

DisableTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DisableTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> DisableTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
