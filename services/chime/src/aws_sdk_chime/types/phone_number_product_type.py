"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberProductType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

PhoneNumberProductType: TypeAlias = Literal[
    "BusinessCalling",
    "VoiceConnector",
    "SipMediaApplicationDialIn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BusinessCalling",
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
