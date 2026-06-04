"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentStrategy``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

DeploymentStrategy: TypeAlias = Literal[
    "ROLLING",
    "BLUE_GREEN",
    "LINEAR",
    "CANARY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROLLING",
        "BLUE_GREEN",
        "LINEAR",
        "CANARY",
    )
)


def serialize_aws_json_1_1(value: DeploymentStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentStrategy value: {data!r}")
    return cast(DeploymentStrategy, data)
