"""Generated from Smithy shape ``com.amazonaws.emr#StepState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

StepState: TypeAlias = Literal[
    "PENDING",
    "CANCEL_PENDING",
    "RUNNING",
    "COMPLETED",
    "CANCELLED",
    "FAILED",
    "INTERRUPTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "CANCEL_PENDING",
        "RUNNING",
        "COMPLETED",
        "CANCELLED",
        "FAILED",
        "INTERRUPTED",
    )
)


def serialize_aws_json_1_1(value: StepState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepState value: {data!r}")
    return cast(StepState, data)
