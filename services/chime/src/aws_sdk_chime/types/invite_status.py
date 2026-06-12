"""Generated from Smithy shape ``com.amazonaws.chime#InviteStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

InviteStatus: TypeAlias = Literal[
    "Pending",
    "Accepted",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Accepted",
        "Failed",
    )
)


def serialize_json(value: InviteStatus) -> str:
    return value


def deserialize_json(data: str) -> InviteStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InviteStatus value: {data!r}")
    return cast(InviteStatus, data)
