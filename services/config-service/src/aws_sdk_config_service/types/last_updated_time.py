"""Generated from Smithy shape ``com.amazonaws.configservice#LastUpdatedTime``."""

import datetime
from typing import TypeAlias

LastUpdatedTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastUpdatedTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastUpdatedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
