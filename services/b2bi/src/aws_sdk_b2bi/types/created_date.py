"""Generated from Smithy shape ``com.amazonaws.b2bi#CreatedDate``."""

import datetime
from typing import TypeAlias

CreatedDate: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatedDate) -> str:
    return value.isoformat()


def deserialize_aws_json_1_0(data: str) -> CreatedDate:
    return datetime.datetime.fromisoformat(data)
