"""Generated from Smithy shape ``com.amazonaws.configservice#LaterTime``."""

import datetime
from typing import TypeAlias

LaterTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LaterTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LaterTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
