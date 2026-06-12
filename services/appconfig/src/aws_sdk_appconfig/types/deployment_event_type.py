"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

DeploymentEventType: TypeAlias = Literal[
    "PERCENTAGE_UPDATED",
    "ROLLBACK_STARTED",
    "ROLLBACK_COMPLETED",
    "BAKE_TIME_STARTED",
    "DEPLOYMENT_STARTED",
    "DEPLOYMENT_COMPLETED",
    "REVERT_COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERCENTAGE_UPDATED",
        "ROLLBACK_STARTED",
        "ROLLBACK_COMPLETED",
        "BAKE_TIME_STARTED",
        "DEPLOYMENT_STARTED",
        "DEPLOYMENT_COMPLETED",
        "REVERT_COMPLETED",
    )
)


def serialize_json(value: DeploymentEventType) -> str:
    return value


def deserialize_json(data: str) -> DeploymentEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentEventType value: {data!r}")
    return cast(DeploymentEventType, data)
