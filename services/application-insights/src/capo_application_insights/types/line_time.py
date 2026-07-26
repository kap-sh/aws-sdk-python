"""Generated from Smithy shape ``com.amazonaws.applicationinsights#LineTime``."""

import datetime
from typing import TypeAlias

LineTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LineTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
