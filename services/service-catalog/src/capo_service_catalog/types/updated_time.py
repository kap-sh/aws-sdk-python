"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdatedTime``."""

import datetime
from typing import TypeAlias

UpdatedTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatedTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> UpdatedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
