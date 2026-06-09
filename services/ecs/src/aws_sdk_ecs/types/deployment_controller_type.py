"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentControllerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

DeploymentControllerType: TypeAlias = Literal[
    "ECS",
    "CODE_DEPLOY",
    "EXTERNAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ECS",
        "CODE_DEPLOY",
        "EXTERNAL",
    )
)


def serialize_aws_json_1_1(value: DeploymentControllerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentControllerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentControllerType value: {data!r}")
    return cast(DeploymentControllerType, data)
