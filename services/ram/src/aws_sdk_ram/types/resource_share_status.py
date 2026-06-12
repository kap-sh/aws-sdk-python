"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

ResourceShareStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "FAILED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
        "FAILED",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: ResourceShareStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceShareStatus value: {data!r}")
    return cast(ResourceShareStatus, data)
