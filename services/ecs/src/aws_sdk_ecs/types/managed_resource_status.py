"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedResourceStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ManagedResourceStatus: TypeAlias = Literal[
    "PROVISIONING",
    "ACTIVE",
    "DEPROVISIONING",
    "DELETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONING",
        "ACTIVE",
        "DEPROVISIONING",
        "DELETED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ManagedResourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedResourceStatus value: {data!r}")
    return cast(ManagedResourceStatus, data)
