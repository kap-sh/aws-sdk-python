"""Generated from Smithy shape ``com.amazonaws.b2bi#ModifiedDate``."""

import datetime
from typing import TypeAlias

ModifiedDate: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModifiedDate) -> str:
    return value.isoformat()


def deserialize_aws_json_1_0(data: str) -> ModifiedDate:
    return datetime.datetime.fromisoformat(data)
