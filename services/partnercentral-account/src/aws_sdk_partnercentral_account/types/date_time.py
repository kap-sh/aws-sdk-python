"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#DateTime``."""

import datetime
from typing import TypeAlias

DateTime: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DateTime) -> str:
    return value.isoformat()


def deserialize_aws_json_1_0(data: str) -> DateTime:
    return datetime.datetime.fromisoformat(data)
