"""Generated from Smithy shape ``com.amazonaws.sagemaker#InvocationStartTime``."""

import datetime
from typing import TypeAlias

InvocationStartTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvocationStartTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> InvocationStartTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
