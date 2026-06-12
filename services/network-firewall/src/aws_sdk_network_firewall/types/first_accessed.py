"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirstAccessed``."""

import datetime
from typing import TypeAlias

FirstAccessed: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirstAccessed) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> FirstAccessed:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
