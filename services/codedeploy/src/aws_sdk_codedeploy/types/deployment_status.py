"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

DeploymentStatus: TypeAlias = Literal[
    "Created",
    "Queued",
    "InProgress",
    "Baking",
    "Succeeded",
    "Failed",
    "Stopped",
    "Ready",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Created",
        "Queued",
        "InProgress",
        "Baking",
        "Succeeded",
        "Failed",
        "Stopped",
        "Ready",
    )
)


def serialize_aws_json_1_1(value: DeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentStatus value: {data!r}")
    return cast(DeploymentStatus, data)
