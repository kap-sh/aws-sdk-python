"""Generated from Smithy shape ``com.amazonaws.amplifybackend#MfaTypesElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

MfaTypesElement: TypeAlias = Literal[
    "SMS",
    "TOTP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SMS",
        "TOTP",
    )
)


def serialize_json(value: MfaTypesElement) -> str:
    return value


def deserialize_json(data: str) -> MfaTypesElement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MfaTypesElement value: {data!r}")
    return cast(MfaTypesElement, data)
