"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#timestamp``."""

import datetime
from typing import TypeAlias

timestamp: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: timestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
