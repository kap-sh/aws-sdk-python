"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberAssociationName``."""

from typing import Literal, TypeAlias, cast

PhoneNumberAssociationName: TypeAlias = Literal[
    "AccountId",
    "UserId",
    "VoiceConnectorId",
    "VoiceConnectorGroupId",
    "SipRuleId",
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberAssociationName) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberAssociationName:
    return cast(PhoneNumberAssociationName, data)
