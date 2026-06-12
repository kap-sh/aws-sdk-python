"""Generated from Smithy shape ``com.amazonaws.gamelift#DeploymentProtectionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

DeploymentProtectionStrategy: TypeAlias = Literal[
    "WITH_PROTECTION",
    "IGNORE_PROTECTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WITH_PROTECTION",
        "IGNORE_PROTECTION",
    )
)


def serialize_aws_json_1_1(value: DeploymentProtectionStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentProtectionStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeploymentProtectionStrategy value: {data!r}"
        )
    return cast(DeploymentProtectionStrategy, data)
