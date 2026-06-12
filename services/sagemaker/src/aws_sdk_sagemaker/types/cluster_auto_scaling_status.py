"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoScalingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterAutoScalingStatus: TypeAlias = Literal[
    "InService",
    "Failed",
    "Creating",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InService",
        "Failed",
        "Creating",
        "Deleting",
    )
)


def serialize_aws_json_1_1(value: ClusterAutoScalingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterAutoScalingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterAutoScalingStatus value: {data!r}")
    return cast(ClusterAutoScalingStatus, data)
