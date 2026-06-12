"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchRebootClusterNodesErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

BatchRebootClusterNodesErrorCode: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: BatchRebootClusterNodesErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchRebootClusterNodesErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchRebootClusterNodesErrorCode value: {data!r}"
        )
    return cast(BatchRebootClusterNodesErrorCode, data)
