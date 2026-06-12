"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

InstanceGroupStatus: TypeAlias = Literal[
    "InService",
    "Creating",
    "Updating",
    "Failed",
    "Degraded",
    "SystemUpdating",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InService",
        "Creating",
        "Updating",
        "Failed",
        "Degraded",
        "SystemUpdating",
        "Deleting",
    )
)


def serialize_aws_json_1_1(value: InstanceGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceGroupStatus value: {data!r}")
    return cast(InstanceGroupStatus, data)
