"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

ServiceDeploymentStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESSFUL",
    "STOPPED",
    "STOP_REQUESTED",
    "IN_PROGRESS",
    "ROLLBACK_REQUESTED",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_SUCCESSFUL",
    "ROLLBACK_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUCCESSFUL",
        "STOPPED",
        "STOP_REQUESTED",
        "IN_PROGRESS",
        "ROLLBACK_REQUESTED",
        "ROLLBACK_IN_PROGRESS",
        "ROLLBACK_SUCCESSFUL",
        "ROLLBACK_FAILED",
    )
)


def serialize_aws_json_1_1(value: ServiceDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceDeploymentStatus value: {data!r}")
    return cast(ServiceDeploymentStatus, data)
