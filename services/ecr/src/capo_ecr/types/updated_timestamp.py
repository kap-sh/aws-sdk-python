"""Generated from Smithy shape ``com.amazonaws.ecr#UpdatedTimestamp``."""

import datetime
from typing import TypeAlias

UpdatedTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatedTimestamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> UpdatedTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
