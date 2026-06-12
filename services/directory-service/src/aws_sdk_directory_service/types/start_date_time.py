"""Generated from Smithy shape ``com.amazonaws.directoryservice#StartDateTime``."""

import datetime
from typing import TypeAlias

StartDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDateTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> StartDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
