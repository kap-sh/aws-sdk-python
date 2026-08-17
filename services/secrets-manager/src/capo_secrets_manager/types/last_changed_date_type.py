"""Generated from Smithy shape ``com.amazonaws.secretsmanager#LastChangedDateType``."""

import datetime
from typing import TypeAlias

LastChangedDateType: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastChangedDateType) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> LastChangedDateType:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
