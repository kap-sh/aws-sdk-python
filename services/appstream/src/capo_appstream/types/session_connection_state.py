"""Generated from Smithy shape ``com.amazonaws.appstream#SessionConnectionState``."""

from typing import Literal, TypeAlias, cast

SessionConnectionState: TypeAlias = Literal[
    "CONNECTED",
    "NOT_CONNECTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionConnectionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionConnectionState:
    return cast(SessionConnectionState, data)
