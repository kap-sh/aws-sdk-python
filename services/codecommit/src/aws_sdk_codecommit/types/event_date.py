"""Generated from Smithy shape ``com.amazonaws.codecommit#EventDate``."""

import datetime
from typing import TypeAlias

EventDate: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDate) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> EventDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
