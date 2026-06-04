"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentRolloutState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

DeploymentRolloutState: TypeAlias = Literal[
    "COMPLETED",
    "FAILED",
    "IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "FAILED",
        "IN_PROGRESS",
    )
)


def serialize_aws_json_1_1(value: DeploymentRolloutState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentRolloutState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentRolloutState value: {data!r}")
    return cast(DeploymentRolloutState, data)
