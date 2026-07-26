"""Generated from Smithy shape ``com.amazonaws.lakeformation#ExpirationTimestamp``."""

import datetime
from typing import TypeAlias

ExpirationTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ExpirationTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> ExpirationTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
