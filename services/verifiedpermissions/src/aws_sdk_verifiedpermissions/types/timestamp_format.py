"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#TimestampFormat``."""

import datetime
from typing import TypeAlias

TimestampFormat: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimestampFormat) -> str:
    return value.isoformat()


def deserialize_aws_json_1_0(data: str) -> TimestampFormat:
    return datetime.datetime.fromisoformat(data)
