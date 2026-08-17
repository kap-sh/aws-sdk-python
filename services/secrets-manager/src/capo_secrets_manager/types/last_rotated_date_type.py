"""Generated from Smithy shape ``com.amazonaws.secretsmanager#LastRotatedDateType``."""

import datetime
from typing import TypeAlias

LastRotatedDateType: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastRotatedDateType) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastRotatedDateType:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
