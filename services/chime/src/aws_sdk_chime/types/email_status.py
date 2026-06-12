"""Generated from Smithy shape ``com.amazonaws.chime#EmailStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

EmailStatus: TypeAlias = Literal[
    "NotSent",
    "Sent",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotSent",
        "Sent",
        "Failed",
    )
)


def serialize_json(value: EmailStatus) -> str:
    return value


def deserialize_json(data: str) -> EmailStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmailStatus value: {data!r}")
    return cast(EmailStatus, data)
