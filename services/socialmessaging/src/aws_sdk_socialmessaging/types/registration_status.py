"""Generated from Smithy shape ``com.amazonaws.socialmessaging#RegistrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_socialmessaging.errors import DeserializationError

RegistrationStatus: TypeAlias = Literal[
    "COMPLETE",
    "INCOMPLETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "INCOMPLETE",
    )
)


def serialize_json(value: RegistrationStatus) -> str:
    return value


def deserialize_json(data: str) -> RegistrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistrationStatus value: {data!r}")
    return cast(RegistrationStatus, data)
