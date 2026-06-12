"""Generated from Smithy shape ``com.amazonaws.ssm#LastResourceDataSyncTime``."""

import datetime
from typing import TypeAlias

LastResourceDataSyncTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastResourceDataSyncTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastResourceDataSyncTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
