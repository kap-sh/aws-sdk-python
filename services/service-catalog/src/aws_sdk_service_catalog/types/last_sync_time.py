"""Generated from Smithy shape ``com.amazonaws.servicecatalog#LastSyncTime``."""

import datetime
from typing import TypeAlias

LastSyncTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastSyncTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastSyncTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
