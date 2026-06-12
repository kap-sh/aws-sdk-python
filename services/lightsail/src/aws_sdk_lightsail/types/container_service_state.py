"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ContainerServiceState: TypeAlias = Literal[
    "PENDING",
    "READY",
    "RUNNING",
    "UPDATING",
    "DELETING",
    "DISABLED",
    "DEPLOYING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "READY",
        "RUNNING",
        "UPDATING",
        "DELETING",
        "DISABLED",
        "DEPLOYING",
    )
)


def serialize_aws_json_1_1(value: ContainerServiceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServiceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerServiceState value: {data!r}")
    return cast(ContainerServiceState, data)
