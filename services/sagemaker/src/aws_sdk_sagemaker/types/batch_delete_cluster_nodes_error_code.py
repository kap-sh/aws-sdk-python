"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDeleteClusterNodesErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

BatchDeleteClusterNodesErrorCode: TypeAlias = Literal[
    "NodeIdNotFound",
    "InvalidNodeStatus",
    "NodeIdInUse",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NodeIdNotFound",
        "InvalidNodeStatus",
        "NodeIdInUse",
    )
)


def serialize_aws_json_1_1(value: BatchDeleteClusterNodesErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchDeleteClusterNodesErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchDeleteClusterNodesErrorCode value: {data!r}"
        )
    return cast(BatchDeleteClusterNodesErrorCode, data)
