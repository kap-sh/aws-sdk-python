"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

ServiceEnvironmentStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "DELETED",
    "VALID",
    "INVALID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "DELETING",
        "DELETED",
        "VALID",
        "INVALID",
    )
)


def serialize_json(value: ServiceEnvironmentStatus) -> str:
    return value


def deserialize_json(data: str) -> ServiceEnvironmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceEnvironmentStatus value: {data!r}")
    return cast(ServiceEnvironmentStatus, data)
