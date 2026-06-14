"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreatedDate``."""

import datetime
from typing import TypeAlias

CreatedDate: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatedDate) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> CreatedDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
