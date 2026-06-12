"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#AssociatePhoneNumbersWithVoiceConnectorGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.e164_phone_number_list
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.nullable_boolean


class AssociatePhoneNumbersWithVoiceConnectorGroupRequest(TypedDict):
    voice_connector_group_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The Amazon Chime SDK Voice Connector group ID.</p>"""
    e164_phone_numbers: (
        "aws_sdk_chime_sdk_voice.types.e164_phone_number_list.E164PhoneNumberList"
    )
    """<p>List of phone numbers, in E.164 format.</p>"""
    force_associate: NotRequired[
        "aws_sdk_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
    ]
    """<p>If true, associates the provided phone numbers with the provided Amazon Chime SDK Voice Connector Group and removes any previously existing associations. If false, does not associate any phone numbers that have previously existing associations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePhoneNumbersWithVoiceConnectorGroupRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_voice.types.e164_phone_number_list

    out["E164PhoneNumbers"] = (
        aws_sdk_chime_sdk_voice.types.e164_phone_number_list.serialize_json(
            value["e164_phone_numbers"]
        )
    )
    if "force_associate" in value:
        out["ForceAssociate"] = value["force_associate"]
    return out


def deserialize_json(data: dict) -> AssociatePhoneNumbersWithVoiceConnectorGroupRequest:
    out: AssociatePhoneNumbersWithVoiceConnectorGroupRequest = {}  # type: ignore[typeddict-item]
    if "E164PhoneNumbers" in data:
        import aws_sdk_chime_sdk_voice.types.e164_phone_number_list

        out["e164_phone_numbers"] = (
            aws_sdk_chime_sdk_voice.types.e164_phone_number_list.deserialize_json(
                data["E164PhoneNumbers"]
            )
        )
    else:
        raise DeserializationError(
            "AssociatePhoneNumbersWithVoiceConnectorGroupRequest.e164_phone_numbers required"
        )
    if "ForceAssociate" in data:
        out["force_associate"] = data["ForceAssociate"]
    return out
