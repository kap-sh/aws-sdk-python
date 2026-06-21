"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchAddClusterNodesErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchAddClusterNodesErrorCode: TypeAlias = Literal[
    "InstanceGroupNotFound",
    "InvalidInstanceGroupStatus",
    "IncompatibleAvailabilityZones",
    "IncompatibleInstanceTypes",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAddClusterNodesErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchAddClusterNodesErrorCode:
    return cast(BatchAddClusterNodesErrorCode, data)
