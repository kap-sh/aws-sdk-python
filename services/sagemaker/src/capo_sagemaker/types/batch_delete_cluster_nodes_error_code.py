"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDeleteClusterNodesErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchDeleteClusterNodesErrorCode: TypeAlias = Literal[
    "NodeIdNotFound",
    "InvalidNodeStatus",
    "NodeIdInUse",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteClusterNodesErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchDeleteClusterNodesErrorCode:
    return cast(BatchDeleteClusterNodesErrorCode, data)
