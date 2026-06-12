"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

DeviceDeploymentStatus: TypeAlias = Literal[
    "READYTODEPLOY",
    "INPROGRESS",
    "DEPLOYED",
    "FAILED",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READYTODEPLOY",
        "INPROGRESS",
        "DEPLOYED",
        "FAILED",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: DeviceDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceDeploymentStatus value: {data!r}")
    return cast(DeviceDeploymentStatus, data)
