"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLJobStatus: TypeAlias = Literal[
    "Completed",
    "InProgress",
    "Failed",
    "Stopped",
    "Stopping",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Completed",
        "InProgress",
        "Failed",
        "Stopped",
        "Stopping",
    )
)


def serialize_aws_json_1_1(value: AutoMLJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLJobStatus value: {data!r}")
    return cast(AutoMLJobStatus, data)
