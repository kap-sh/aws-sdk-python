"""Generated from Smithy shape ``com.amazonaws.configservice#EarlierTime``."""

import datetime
from typing import TypeAlias

EarlierTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EarlierTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> EarlierTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
