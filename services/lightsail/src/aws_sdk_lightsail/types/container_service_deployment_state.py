"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceDeploymentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ContainerServiceDeploymentState: TypeAlias = Literal[
    "ACTIVATING",
    "ACTIVE",
    "INACTIVE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVATING",
        "ACTIVE",
        "INACTIVE",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ContainerServiceDeploymentState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServiceDeploymentState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContainerServiceDeploymentState value: {data!r}"
        )
    return cast(ContainerServiceDeploymentState, data)
