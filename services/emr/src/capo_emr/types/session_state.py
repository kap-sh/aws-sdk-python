"""Generated from Smithy shape ``com.amazonaws.emr#SessionState``."""

from typing import Literal, TypeAlias, cast

SessionState: TypeAlias = Literal[
    "SUBMITTED",
    "STARTING",
    "STARTED",
    "IDLE",
    "BUSY",
    "TERMINATING",
    "TERMINATED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionState:
    return cast(SessionState, data)
