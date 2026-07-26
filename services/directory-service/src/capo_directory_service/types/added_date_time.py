"""Generated from Smithy shape ``com.amazonaws.directoryservice#AddedDateTime``."""

import datetime
from typing import TypeAlias

AddedDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddedDateTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> AddedDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
