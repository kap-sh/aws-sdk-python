"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Timestamp``."""

import datetime
from typing import TypeAlias

Timestamp: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Timestamp) -> str:
    return value.isoformat()


def deserialize_aws_json_1_0(data: str) -> Timestamp:
    return datetime.datetime.fromisoformat(data)
