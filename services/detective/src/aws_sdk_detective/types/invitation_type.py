"""Generated from Smithy shape ``com.amazonaws.detective#InvitationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

InvitationType: TypeAlias = Literal[
    "INVITATION",
    "ORGANIZATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVITATION",
        "ORGANIZATION",
    )
)


def serialize_json(value: InvitationType) -> str:
    return value


def deserialize_json(data: str) -> InvitationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvitationType value: {data!r}")
    return cast(InvitationType, data)
