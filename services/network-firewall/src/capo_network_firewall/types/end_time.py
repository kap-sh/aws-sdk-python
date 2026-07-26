"""Generated from Smithy shape ``com.amazonaws.networkfirewall#EndTime``."""

import datetime
from typing import TypeAlias

EndTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EndTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> EndTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
