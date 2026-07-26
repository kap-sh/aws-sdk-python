"""Generated from Smithy shape ``com.amazonaws.ecr#LastActivatedAtTimestamp``."""

import datetime
from typing import TypeAlias

LastActivatedAtTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastActivatedAtTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastActivatedAtTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
