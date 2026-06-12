"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberOrderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

PhoneNumberOrderType: TypeAlias = Literal[
    "New",
    "Porting",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "New",
        "Porting",
    )
)


def serialize_json(value: PhoneNumberOrderType) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberOrderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhoneNumberOrderType value: {data!r}")
    return cast(PhoneNumberOrderType, data)
