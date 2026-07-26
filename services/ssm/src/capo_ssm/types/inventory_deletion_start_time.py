"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryDeletionStartTime``."""

import datetime
from typing import TypeAlias

InventoryDeletionStartTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryDeletionStartTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> InventoryDeletionStartTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
