"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricQueryStartTimestamp``."""

import datetime
from typing import TypeAlias

MetricQueryStartTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryStartTimestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> MetricQueryStartTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
