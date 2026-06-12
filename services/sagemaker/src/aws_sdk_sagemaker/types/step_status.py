"""Generated from Smithy shape ``com.amazonaws.sagemaker#StepStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

StepStatus: TypeAlias = Literal[
    "Starting",
    "Executing",
    "Stopping",
    "Stopped",
    "Failed",
    "Succeeded",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Starting",
        "Executing",
        "Stopping",
        "Stopped",
        "Failed",
        "Succeeded",
    )
)


def serialize_aws_json_1_1(value: StepStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepStatus value: {data!r}")
    return cast(StepStatus, data)
