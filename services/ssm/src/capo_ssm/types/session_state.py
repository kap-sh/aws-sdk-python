"""Generated from Smithy shape ``com.amazonaws.ssm#SessionState``."""

from typing import Literal, TypeAlias, cast

SessionState: TypeAlias = Literal[
    "Active",
    "History",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionState:
    return cast(SessionState, data)
