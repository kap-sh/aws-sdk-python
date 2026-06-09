"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

DeploymentLifecycleHookStatus: TypeAlias = Literal[
    "AWAITING_ACTION",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWAITING_ACTION",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "TIMED_OUT",
    )
)


def serialize_aws_json_1_1(value: DeploymentLifecycleHookStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentLifecycleHookStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeploymentLifecycleHookStatus value: {data!r}"
        )
    return cast(DeploymentLifecycleHookStatus, data)
