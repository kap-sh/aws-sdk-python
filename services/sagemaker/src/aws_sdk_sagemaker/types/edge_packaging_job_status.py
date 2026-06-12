"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgePackagingJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

EdgePackagingJobStatus: TypeAlias = Literal[
    "STARTING",
    "INPROGRESS",
    "COMPLETED",
    "FAILED",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "INPROGRESS",
        "COMPLETED",
        "FAILED",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: EdgePackagingJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EdgePackagingJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EdgePackagingJobStatus value: {data!r}")
    return cast(EdgePackagingJobStatus, data)
