"""Generated from Smithy shape ``com.amazonaws.managedblockchain#InvitationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

InvitationStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "ACCEPTING",
    "REJECTED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACCEPTED",
        "ACCEPTING",
        "REJECTED",
        "EXPIRED",
    )
)


def serialize_json(value: InvitationStatus) -> str:
    return value


def deserialize_json(data: str) -> InvitationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvitationStatus value: {data!r}")
    return cast(InvitationStatus, data)
