"""Generated from Smithy shape ``com.amazonaws.dax#SSEStatus``."""

from typing import Literal, TypeAlias, cast

SSEStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SSEStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SSEStatus:
    return cast(SSEStatus, data)
