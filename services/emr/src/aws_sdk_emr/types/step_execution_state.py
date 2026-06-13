"""Generated from Smithy shape ``com.amazonaws.emr#StepExecutionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

StepExecutionState: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "CONTINUE",
    "COMPLETED",
    "CANCELLED",
    "FAILED",
    "INTERRUPTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "RUNNING",
        "CONTINUE",
        "COMPLETED",
        "CANCELLED",
        "FAILED",
        "INTERRUPTED",
    )
)


def serialize_aws_json_1_1(value: StepExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepExecutionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepExecutionState value: {data!r}")
    return cast(StepExecutionState, data)
