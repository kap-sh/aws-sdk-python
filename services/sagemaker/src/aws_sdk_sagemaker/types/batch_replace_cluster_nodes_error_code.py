"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchReplaceClusterNodesErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

BatchReplaceClusterNodesErrorCode: TypeAlias = Literal[
    "InstanceIdNotFound",
    "InvalidInstanceStatus",
    "InstanceIdInUse",
    "InternalServerError",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InstanceIdNotFound",
        "InvalidInstanceStatus",
        "InstanceIdInUse",
        "InternalServerError",
    )
)


def serialize_aws_json_1_1(value: BatchReplaceClusterNodesErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchReplaceClusterNodesErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchReplaceClusterNodesErrorCode value: {data!r}"
        )
    return cast(BatchReplaceClusterNodesErrorCode, data)
