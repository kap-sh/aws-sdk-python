"""Generated from Smithy shape ``com.amazonaws.glue#StatementState``."""

from typing import Literal, TypeAlias, cast

StatementState: TypeAlias = Literal[
    "WAITING",
    "RUNNING",
    "AVAILABLE",
    "CANCELLING",
    "CANCELLED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatementState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatementState:
    return cast(StatementState, data)
