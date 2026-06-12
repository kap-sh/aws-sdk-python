"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgePresetDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

EdgePresetDeploymentStatus: TypeAlias = Literal[
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: EdgePresetDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EdgePresetDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EdgePresetDeploymentStatus value: {data!r}"
        )
    return cast(EdgePresetDeploymentStatus, data)
