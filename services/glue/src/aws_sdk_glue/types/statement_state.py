"""Generated from Smithy shape ``com.amazonaws.glue#StatementState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

StatementState: TypeAlias = Literal[
    "WAITING",
    "RUNNING",
    "AVAILABLE",
    "CANCELLING",
    "CANCELLED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WAITING",
        "RUNNING",
        "AVAILABLE",
        "CANCELLING",
        "CANCELLED",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: StatementState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatementState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatementState value: {data!r}")
    return cast(StatementState, data)
