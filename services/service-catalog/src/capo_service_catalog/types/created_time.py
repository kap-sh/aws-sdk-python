"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreatedTime``."""

import datetime
from typing import TypeAlias

CreatedTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatedTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> CreatedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
