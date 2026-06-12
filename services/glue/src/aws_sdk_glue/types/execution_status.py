"""Generated from Smithy shape ``com.amazonaws.glue#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "FAILED",
    "STARTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "STARTED",
    )
)


def serialize_aws_json_1_1(value: ExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)
