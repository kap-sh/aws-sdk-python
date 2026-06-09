"""Generated from Smithy shape ``com.amazonaws.secretsmanager#TimestampType``."""

import datetime
from typing import TypeAlias

TimestampType: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimestampType) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> TimestampType:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
