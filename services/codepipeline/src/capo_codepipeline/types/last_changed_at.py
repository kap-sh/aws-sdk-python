"""Generated from Smithy shape ``com.amazonaws.codepipeline#LastChangedAt``."""

import datetime
from typing import TypeAlias

LastChangedAt: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastChangedAt) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastChangedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
