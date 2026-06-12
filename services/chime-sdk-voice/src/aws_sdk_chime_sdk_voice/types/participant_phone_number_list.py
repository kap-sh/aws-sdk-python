"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ParticipantPhoneNumberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.e164_phone_number

ParticipantPhoneNumberList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantPhoneNumberList) -> list:
    return list(value)


def deserialize_json(data: list) -> ParticipantPhoneNumberList:
    return list(data)
