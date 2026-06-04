"""Generated from Smithy shape ``com.amazonaws.ecs#ResourceManagementType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ResourceManagementType: TypeAlias = Literal[
    "CUSTOMER",
    "ECS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER",
        "ECS",
    )
)


def serialize_aws_json_1_1(value: ResourceManagementType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceManagementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceManagementType value: {data!r}")
    return cast(ResourceManagementType, data)
