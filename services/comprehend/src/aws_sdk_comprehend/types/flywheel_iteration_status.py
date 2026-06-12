"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelIterationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

FlywheelIterationStatus: TypeAlias = Literal[
    "TRAINING",
    "EVALUATING",
    "COMPLETED",
    "FAILED",
    "STOP_REQUESTED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRAINING",
        "EVALUATING",
        "COMPLETED",
        "FAILED",
        "STOP_REQUESTED",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: FlywheelIterationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlywheelIterationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlywheelIterationStatus value: {data!r}")
    return cast(FlywheelIterationStatus, data)
