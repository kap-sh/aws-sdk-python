"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateTime``."""

import datetime
from typing import TypeAlias

UpdateTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> UpdateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
