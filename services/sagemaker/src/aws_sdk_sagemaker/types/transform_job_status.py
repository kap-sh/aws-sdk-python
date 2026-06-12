"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TransformJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_aws_json_1_1(value: TransformJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransformJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransformJobStatus value: {data!r}")
    return cast(TransformJobStatus, data)
