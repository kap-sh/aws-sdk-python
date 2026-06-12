"""Generated from Smithy shape ``com.amazonaws.route53profiles#Rfc3339Timestamp``."""

import datetime
from typing import TypeAlias

Rfc3339Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Rfc3339Timestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> Rfc3339Timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
