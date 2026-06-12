"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DeploymentTarget``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

DeploymentTarget: TypeAlias = Literal[
    "GREENGRASS",
    "CLOUD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GREENGRASS",
        "CLOUD",
    )
)


def serialize_aws_json_1_1(value: DeploymentTarget) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentTarget:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentTarget value: {data!r}")
    return cast(DeploymentTarget, data)
