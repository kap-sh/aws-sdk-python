"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

ResourceShareInvitationStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "REJECTED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACCEPTED",
        "REJECTED",
        "EXPIRED",
    )
)


def serialize_json(value: ResourceShareInvitationStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareInvitationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceShareInvitationStatus value: {data!r}"
        )
    return cast(ResourceShareInvitationStatus, data)
