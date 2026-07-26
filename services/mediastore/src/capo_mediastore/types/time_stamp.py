"""Generated from Smithy shape ``com.amazonaws.mediastore#TimeStamp``."""

import datetime
from typing import TypeAlias

TimeStamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeStamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> TimeStamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
