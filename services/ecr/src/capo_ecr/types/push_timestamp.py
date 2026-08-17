"""Generated from Smithy shape ``com.amazonaws.ecr#PushTimestamp``."""

import datetime
from typing import TypeAlias

PushTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PushTimestamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> PushTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
