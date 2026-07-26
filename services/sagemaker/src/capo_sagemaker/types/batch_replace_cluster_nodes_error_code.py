"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchReplaceClusterNodesErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchReplaceClusterNodesErrorCode: TypeAlias = Literal[
    "InstanceIdNotFound",
    "InvalidInstanceStatus",
    "InstanceIdInUse",
    "InternalServerError",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchReplaceClusterNodesErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchReplaceClusterNodesErrorCode:
    return cast(BatchReplaceClusterNodesErrorCode, data)
