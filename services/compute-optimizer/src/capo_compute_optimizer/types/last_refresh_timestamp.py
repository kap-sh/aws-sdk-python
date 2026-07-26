"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LastRefreshTimestamp``."""

import datetime
from typing import TypeAlias

LastRefreshTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LastRefreshTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> LastRefreshTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
