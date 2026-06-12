"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#RequestedTime``."""

import datetime
from typing import TypeAlias

RequestedTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestedTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> RequestedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
