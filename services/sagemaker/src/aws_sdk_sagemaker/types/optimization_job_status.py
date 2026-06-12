"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

OptimizationJobStatus: TypeAlias = Literal[
    "INPROGRESS",
    "COMPLETED",
    "FAILED",
    "STARTING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INPROGRESS",
        "COMPLETED",
        "FAILED",
        "STARTING",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: OptimizationJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptimizationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OptimizationJobStatus value: {data!r}")
    return cast(OptimizationJobStatus, data)
