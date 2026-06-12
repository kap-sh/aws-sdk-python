"""Generated from Smithy shape ``com.amazonaws.amplify#LastDeployTime``."""

import datetime
from typing import TypeAlias

LastDeployTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastDeployTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> LastDeployTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
