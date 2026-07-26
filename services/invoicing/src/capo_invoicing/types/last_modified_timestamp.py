"""Generated from Smithy shape ``com.amazonaws.invoicing#LastModifiedTimestamp``."""

import datetime
from typing import TypeAlias

LastModifiedTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LastModifiedTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> LastModifiedTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
