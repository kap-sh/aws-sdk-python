"""Generated from Smithy shape ``com.amazonaws.managedblockchain#AccessorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

AccessorStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING_DELETION",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PENDING_DELETION",
        "DELETED",
    )
)


def serialize_json(value: AccessorStatus) -> str:
    return value


def deserialize_json(data: str) -> AccessorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessorStatus value: {data!r}")
    return cast(AccessorStatus, data)
