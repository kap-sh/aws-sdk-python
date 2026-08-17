"""Generated from Smithy shape ``com.amazonaws.ecr#RecordedPullTimestamp``."""

import datetime
from typing import TypeAlias

RecordedPullTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordedPullTimestamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> RecordedPullTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
