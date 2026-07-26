"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreatedDateTime``."""

import datetime
from typing import TypeAlias

CreatedDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatedDateTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> CreatedDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
