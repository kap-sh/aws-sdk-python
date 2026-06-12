"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LastAccessed``."""

import datetime
from typing import TypeAlias

LastAccessed: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LastAccessed) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> LastAccessed:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
