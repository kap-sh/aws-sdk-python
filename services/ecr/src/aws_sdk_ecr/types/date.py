"""Generated from Smithy shape ``com.amazonaws.ecr#Date``."""

import datetime
from typing import TypeAlias

Date: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Date) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> Date:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
