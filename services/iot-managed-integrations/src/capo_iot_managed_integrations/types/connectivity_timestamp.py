"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConnectivityTimestamp``."""

import datetime
from typing import TypeAlias

ConnectivityTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ConnectivityTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> ConnectivityTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
