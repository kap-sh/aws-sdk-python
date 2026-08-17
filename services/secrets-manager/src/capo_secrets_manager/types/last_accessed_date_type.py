"""Generated from Smithy shape ``com.amazonaws.secretsmanager#LastAccessedDateType``."""

import datetime
from typing import TypeAlias

LastAccessedDateType: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastAccessedDateType) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastAccessedDateType:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
