"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

ResourceShareAssociationStatus: TypeAlias = Literal[
    "ASSOCIATING",
    "ASSOCIATED",
    "FAILED",
    "DISASSOCIATING",
    "DISASSOCIATED",
    "SUSPENDED",
    "SUSPENDING",
    "RESTORING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSOCIATING",
        "ASSOCIATED",
        "FAILED",
        "DISASSOCIATING",
        "DISASSOCIATED",
        "SUSPENDED",
        "SUSPENDING",
        "RESTORING",
    )
)


def serialize_json(value: ResourceShareAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceShareAssociationStatus value: {data!r}"
        )
    return cast(ResourceShareAssociationStatus, data)
