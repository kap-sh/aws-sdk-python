"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ContainerFleetStatus: TypeAlias = Literal[
    "PENDING",
    "CREATING",
    "CREATED",
    "ACTIVATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "CREATING",
        "CREATED",
        "ACTIVATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: ContainerFleetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerFleetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerFleetStatus value: {data!r}")
    return cast(ContainerFleetStatus, data)
