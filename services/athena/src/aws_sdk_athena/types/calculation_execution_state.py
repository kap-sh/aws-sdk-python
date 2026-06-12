"""Generated from Smithy shape ``com.amazonaws.athena#CalculationExecutionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

CalculationExecutionState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "QUEUED",
    "RUNNING",
    "CANCELING",
    "CANCELED",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "QUEUED",
        "RUNNING",
        "CANCELING",
        "CANCELED",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: CalculationExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CalculationExecutionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CalculationExecutionState value: {data!r}")
    return cast(CalculationExecutionState, data)
