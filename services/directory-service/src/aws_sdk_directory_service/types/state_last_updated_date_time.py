"""Generated from Smithy shape ``com.amazonaws.directoryservice#StateLastUpdatedDateTime``."""

import datetime
from typing import TypeAlias

StateLastUpdatedDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StateLastUpdatedDateTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> StateLastUpdatedDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
