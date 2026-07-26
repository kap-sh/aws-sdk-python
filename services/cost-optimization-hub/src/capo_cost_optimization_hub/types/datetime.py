"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Datetime``."""

import datetime
from typing import TypeAlias

Datetime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Datetime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> Datetime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
