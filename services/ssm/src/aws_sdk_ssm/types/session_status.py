"""Generated from Smithy shape ``com.amazonaws.ssm#SessionStatus``."""

from typing import Literal, TypeAlias, cast

SessionStatus: TypeAlias = Literal[
    "Connected",
    "Connecting",
    "Disconnected",
    "Terminated",
    "Terminating",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionStatus:
    return cast(SessionStatus, data)
