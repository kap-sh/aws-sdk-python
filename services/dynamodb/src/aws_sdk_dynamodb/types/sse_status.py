"""Generated from Smithy shape ``com.amazonaws.dynamodb#SSEStatus``."""

from typing import Literal, TypeAlias, cast

SSEStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SSEStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SSEStatus:
    return cast(SSEStatus, data)
