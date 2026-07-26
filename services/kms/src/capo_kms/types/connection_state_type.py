"""Generated from Smithy shape ``com.amazonaws.kms#ConnectionStateType``."""

from typing import Literal, TypeAlias, cast

ConnectionStateType: TypeAlias = Literal[
    "CONNECTED",
    "CONNECTING",
    "FAILED",
    "DISCONNECTED",
    "DISCONNECTING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionStateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionStateType:
    return cast(ConnectionStateType, data)
