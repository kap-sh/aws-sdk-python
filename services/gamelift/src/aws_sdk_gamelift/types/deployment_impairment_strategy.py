"""Generated from Smithy shape ``com.amazonaws.gamelift#DeploymentImpairmentStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

DeploymentImpairmentStrategy: TypeAlias = Literal[
    "MAINTAIN",
    "ROLLBACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAINTAIN",
        "ROLLBACK",
    )
)


def serialize_aws_json_1_1(value: DeploymentImpairmentStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentImpairmentStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeploymentImpairmentStrategy value: {data!r}"
        )
    return cast(DeploymentImpairmentStrategy, data)
