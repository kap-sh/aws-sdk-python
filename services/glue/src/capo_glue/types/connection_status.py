"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

ConnectionStatus: TypeAlias = Literal[
    "READY",
    "IN_PROGRESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionStatus:
    return cast(ConnectionStatus, data)
