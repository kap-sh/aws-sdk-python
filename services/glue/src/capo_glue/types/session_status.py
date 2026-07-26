"""Generated from Smithy shape ``com.amazonaws.glue#SessionStatus``."""

from typing import Literal, TypeAlias, cast

SessionStatus: TypeAlias = Literal[
    "PROVISIONING",
    "READY",
    "FAILED",
    "TIMEOUT",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionStatus:
    return cast(SessionStatus, data)
