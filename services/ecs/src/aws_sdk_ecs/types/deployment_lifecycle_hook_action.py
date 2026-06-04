"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookAction``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

DeploymentLifecycleHookAction: TypeAlias = Literal[
    "ROLLBACK",
    "CONTINUE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROLLBACK",
        "CONTINUE",
    )
)


def serialize_aws_json_1_1(value: DeploymentLifecycleHookAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentLifecycleHookAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeploymentLifecycleHookAction value: {data!r}"
        )
    return cast(DeploymentLifecycleHookAction, data)
