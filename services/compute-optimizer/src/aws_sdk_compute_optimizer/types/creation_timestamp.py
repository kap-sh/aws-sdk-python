"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CreationTimestamp``."""

import datetime
from typing import TypeAlias

CreationTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreationTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> CreationTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
