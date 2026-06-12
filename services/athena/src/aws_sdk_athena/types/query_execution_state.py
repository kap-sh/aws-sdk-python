"""Generated from Smithy shape ``com.amazonaws.athena#QueryExecutionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

QueryExecutionState: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "CANCELLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
    )
)


def serialize_aws_json_1_1(value: QueryExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryExecutionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryExecutionState value: {data!r}")
    return cast(QueryExecutionState, data)
