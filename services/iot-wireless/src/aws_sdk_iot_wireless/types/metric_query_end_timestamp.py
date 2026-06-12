"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricQueryEndTimestamp``."""

import datetime
from typing import TypeAlias

MetricQueryEndTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryEndTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> MetricQueryEndTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
