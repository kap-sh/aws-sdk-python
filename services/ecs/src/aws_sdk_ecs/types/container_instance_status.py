"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstanceStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ContainerInstanceStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
    "REGISTERING",
    "DEREGISTERING",
    "REGISTRATION_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DRAINING",
        "REGISTERING",
        "DEREGISTERING",
        "REGISTRATION_FAILED",
    )
)


def serialize_aws_json_1_1(value: ContainerInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerInstanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerInstanceStatus value: {data!r}")
    return cast(ContainerInstanceStatus, data)
