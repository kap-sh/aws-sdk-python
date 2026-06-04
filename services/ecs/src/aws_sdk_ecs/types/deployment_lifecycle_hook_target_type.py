"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookTargetType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

DeploymentLifecycleHookTargetType: TypeAlias = Literal[
    "AWS_LAMBDA",
    "PAUSE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_LAMBDA",
        "PAUSE",
    )
)


def serialize_aws_json_1_1(value: DeploymentLifecycleHookTargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentLifecycleHookTargetType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeploymentLifecycleHookTargetType value: {data!r}"
        )
    return cast(DeploymentLifecycleHookTargetType, data)
