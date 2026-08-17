"""Generated from Smithy shape ``com.amazonaws.eventbridge#EventTime``."""

import datetime
from typing import TypeAlias

EventTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> EventTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
