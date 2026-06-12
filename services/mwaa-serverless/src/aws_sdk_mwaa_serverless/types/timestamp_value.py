"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#TimestampValue``."""

import datetime
from typing import TypeAlias

TimestampValue: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimestampValue) -> str:
    return value.isoformat()


def deserialize_aws_json_1_0(data: str) -> TimestampValue:
    return datetime.datetime.fromisoformat(data)
