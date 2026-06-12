"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StartTime``."""

import datetime
from typing import TypeAlias

StartTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> StartTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
