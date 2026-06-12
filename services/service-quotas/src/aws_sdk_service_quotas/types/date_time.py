"""Generated from Smithy shape ``com.amazonaws.servicequotas#DateTime``."""

import datetime
from typing import TypeAlias

DateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DateTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> DateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
