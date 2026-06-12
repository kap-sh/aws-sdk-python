"""Generated from Smithy shape ``com.amazonaws.applicationinsights#EndTime``."""

import datetime
from typing import TypeAlias

EndTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> EndTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
