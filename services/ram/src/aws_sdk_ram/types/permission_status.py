"""Generated from Smithy shape ``com.amazonaws.ram#PermissionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

PermissionStatus: TypeAlias = Literal[
    "ATTACHABLE",
    "UNATTACHABLE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATTACHABLE",
        "UNATTACHABLE",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: PermissionStatus) -> str:
    return value


def deserialize_json(data: str) -> PermissionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionStatus value: {data!r}")
    return cast(PermissionStatus, data)
