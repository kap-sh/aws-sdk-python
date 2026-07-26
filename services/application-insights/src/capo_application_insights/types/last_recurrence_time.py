"""Generated from Smithy shape ``com.amazonaws.applicationinsights#LastRecurrenceTime``."""

import datetime
from typing import TypeAlias

LastRecurrenceTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastRecurrenceTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastRecurrenceTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
