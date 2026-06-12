"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DatetimeAttributeValue``."""

import datetime
from typing import TypeAlias

DatetimeAttributeValue: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DatetimeAttributeValue) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> DatetimeAttributeValue:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
