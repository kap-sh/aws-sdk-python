"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberAssociationName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

PhoneNumberAssociationName: TypeAlias = Literal[
    "AccountId",
    "UserId",
    "VoiceConnectorId",
    "VoiceConnectorGroupId",
    "SipRuleId",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccountId",
        "UserId",
        "VoiceConnectorId",
        "VoiceConnectorGroupId",
        "SipRuleId",
    )
)


def serialize_json(value: PhoneNumberAssociationName) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberAssociationName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PhoneNumberAssociationName value: {data!r}"
        )
    return cast(PhoneNumberAssociationName, data)
