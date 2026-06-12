"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterStatus: TypeAlias = Literal[
    "Creating",
    "Deleting",
    "Failed",
    "InService",
    "RollingBack",
    "SystemUpdating",
    "Updating",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Deleting",
        "Failed",
        "InService",
        "RollingBack",
        "SystemUpdating",
        "Updating",
    )
)


def serialize_aws_json_1_1(value: ClusterStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterStatus value: {data!r}")
    return cast(ClusterStatus, data)
