"""Generated from Smithy shape ``com.amazonaws.fsx#StartTime``."""

import datetime
from typing import TypeAlias

StartTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> StartTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
