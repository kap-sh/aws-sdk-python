"""Generated from Smithy shape ``com.amazonaws.invoicing#AsOfTimestamp``."""

import datetime
from typing import TypeAlias

AsOfTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AsOfTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> AsOfTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
