"""Generated from Smithy shape ``com.amazonaws.ecr#ScanTimestamp``."""

import datetime
from typing import TypeAlias

ScanTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanTimestamp) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ScanTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
