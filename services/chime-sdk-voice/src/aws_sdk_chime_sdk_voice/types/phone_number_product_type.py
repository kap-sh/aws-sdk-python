"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberProductType``."""

from typing import Literal, TypeAlias, cast

PhoneNumberProductType: TypeAlias = Literal[
    "VoiceConnector",
    "SipMediaApplicationDialIn",
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberProductType) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberProductType:
    return cast(PhoneNumberProductType, data)
