"""Generated from Smithy shape ``com.amazonaws.dynamodb#Date``."""

import datetime
from typing import TypeAlias

Date: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Date) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> Date:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
