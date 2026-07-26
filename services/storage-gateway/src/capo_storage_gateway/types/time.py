"""Generated from Smithy shape ``com.amazonaws.storagegateway#Time``."""

import datetime
from typing import TypeAlias

Time: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Time) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> Time:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
