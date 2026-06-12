"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchAddClusterNodesErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

BatchAddClusterNodesErrorCode: TypeAlias = Literal[
    "InstanceGroupNotFound",
    "InvalidInstanceGroupStatus",
    "IncompatibleAvailabilityZones",
    "IncompatibleInstanceTypes",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InstanceGroupNotFound",
        "InvalidInstanceGroupStatus",
        "IncompatibleAvailabilityZones",
        "IncompatibleInstanceTypes",
    )
)


def serialize_aws_json_1_1(value: BatchAddClusterNodesErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchAddClusterNodesErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchAddClusterNodesErrorCode value: {data!r}"
        )
    return cast(BatchAddClusterNodesErrorCode, data)
