"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberProductType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

PhoneNumberProductType: TypeAlias = Literal[
    "VoiceConnector",
    "SipMediaApplicationDialIn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VoiceConnector",
        "SipMediaApplicationDialIn",
    )
)


def serialize_json(value: PhoneNumberProductType) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberProductType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhoneNumberProductType value: {data!r}")
    return cast(PhoneNumberProductType, data)
