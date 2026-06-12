"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#CreatedTimestamp``."""

import datetime
from typing import TypeAlias

CreatedTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreatedTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CreatedTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
