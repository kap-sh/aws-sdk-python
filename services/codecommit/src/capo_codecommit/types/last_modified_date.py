"""Generated from Smithy shape ``com.amazonaws.codecommit#LastModifiedDate``."""

import datetime
from typing import TypeAlias

LastModifiedDate: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastModifiedDate) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastModifiedDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
