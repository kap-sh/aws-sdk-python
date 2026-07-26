"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchRebootClusterNodesErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchRebootClusterNodesErrorCode: TypeAlias = Literal[
    "InstanceIdNotFound",
    "InvalidInstanceStatus",
    "InstanceIdInUse",
    "InternalServerError",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchRebootClusterNodesErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchRebootClusterNodesErrorCode:
    return cast(BatchRebootClusterNodesErrorCode, data)
