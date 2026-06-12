"""Generated from Smithy shape ``com.amazonaws.glue#TimestampValue``."""

import datetime
from typing import TypeAlias

TimestampValue: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimestampValue) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> TimestampValue:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
