"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateTime``."""

import datetime
from typing import TypeAlias

CreateTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> CreateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
