"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DisassociatePhoneNumbersFromVoiceConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.e164_phone_number_list
    import capo_chime_sdk_voice.types.non_empty_string


class DisassociatePhoneNumbersFromVoiceConnectorRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""
    e164_phone_numbers: (
        "capo_chime_sdk_voice.types.e164_phone_number_list.E164PhoneNumberList"
    )
    """<p>List of phone numbers, in E.164 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociatePhoneNumbersFromVoiceConnectorRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.e164_phone_number_list

    out["E164PhoneNumbers"] = (
        capo_chime_sdk_voice.types.e164_phone_number_list.serialize_json(
            value["e164_phone_numbers"]
        )
    )
    return out


def deserialize_json(data: dict) -> DisassociatePhoneNumbersFromVoiceConnectorRequest:
    out: DisassociatePhoneNumbersFromVoiceConnectorRequest = {}  # type: ignore[typeddict-item]
    if "E164PhoneNumbers" in data:
        import capo_chime_sdk_voice.types.e164_phone_number_list

        out["e164_phone_numbers"] = (
            capo_chime_sdk_voice.types.e164_phone_number_list.deserialize_json(
                data["E164PhoneNumbers"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociatePhoneNumbersFromVoiceConnectorRequest.e164_phone_numbers required"
        )
    return out
