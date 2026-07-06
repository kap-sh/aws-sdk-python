"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorProxyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.boolean
    import aws_sdk_chime_sdk_voice.types.country_list
    import aws_sdk_chime_sdk_voice.types.e164_phone_number
    import aws_sdk_chime_sdk_voice.types.integer
    import aws_sdk_chime_sdk_voice.types.non_empty_string128


class PutVoiceConnectorProxyRequest(TypedDict, closed=True):
    voice_connector_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""
    default_session_expiry_minutes: "aws_sdk_chime_sdk_voice.types.integer.Integer"
    """<p>The default number of minutes allowed for proxy session.</p>"""
    phone_number_pool_countries: (
        "aws_sdk_chime_sdk_voice.types.country_list.CountryList"
    )
    """<p>The countries for proxy phone numbers to be selected from.</p>"""
    fall_back_phone_number: NotRequired[
        "aws_sdk_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The phone number to route calls to after a proxy session expires.</p>"""
    disabled: NotRequired["aws_sdk_chime_sdk_voice.types.boolean.Boolean"]
    """<p>When true, stops proxy sessions from being created on the specified Amazon Chime SDK Voice Connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorProxyRequest) -> dict:
    out: dict = {}
    out["DefaultSessionExpiryMinutes"] = value["default_session_expiry_minutes"]
    import aws_sdk_chime_sdk_voice.types.country_list

    out["PhoneNumberPoolCountries"] = (
        aws_sdk_chime_sdk_voice.types.country_list.serialize_json(
            value["phone_number_pool_countries"]
        )
    )
    if "fall_back_phone_number" in value:
        out["FallBackPhoneNumber"] = value["fall_back_phone_number"]
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorProxyRequest:
    out: PutVoiceConnectorProxyRequest = {}  # type: ignore[typeddict-item]
    if "DefaultSessionExpiryMinutes" in data:
        out["default_session_expiry_minutes"] = data["DefaultSessionExpiryMinutes"]
    else:
        raise DeserializationError(
            "PutVoiceConnectorProxyRequest.default_session_expiry_minutes required"
        )
    if "PhoneNumberPoolCountries" in data:
        import aws_sdk_chime_sdk_voice.types.country_list

        out["phone_number_pool_countries"] = (
            aws_sdk_chime_sdk_voice.types.country_list.deserialize_json(
                data["PhoneNumberPoolCountries"]
            )
        )
    else:
        raise DeserializationError(
            "PutVoiceConnectorProxyRequest.phone_number_pool_countries required"
        )
    if "FallBackPhoneNumber" in data:
        out["fall_back_phone_number"] = data["FallBackPhoneNumber"]
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    return out
