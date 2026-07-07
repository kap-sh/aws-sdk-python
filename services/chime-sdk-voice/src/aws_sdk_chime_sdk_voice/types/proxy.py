"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Proxy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.boolean
    import aws_sdk_chime_sdk_voice.types.e164_phone_number
    import aws_sdk_chime_sdk_voice.types.integer
    import aws_sdk_chime_sdk_voice.types.string_list


class Proxy(TypedDict, closed=True):
    default_session_expiry_minutes: NotRequired[
        "aws_sdk_chime_sdk_voice.types.integer.Integer"
    ]
    """<p>The default number of minutes allowed for proxy sessions.</p>"""
    disabled: NotRequired["aws_sdk_chime_sdk_voice.types.boolean.Boolean"]
    """<p>When true, stops proxy sessions from being created on the specified Amazon Chime SDK Voice Connector.</p>"""
    fall_back_phone_number: NotRequired[
        "aws_sdk_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The phone number to route calls to after a proxy session expires.</p>"""
    phone_number_countries: NotRequired[
        "aws_sdk_chime_sdk_voice.types.string_list.StringList"
    ]
    """<p>The countries for proxy phone numbers to be selected from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Proxy) -> dict:
    out: dict = {}
    if "default_session_expiry_minutes" in value:
        out["DefaultSessionExpiryMinutes"] = value["default_session_expiry_minutes"]
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    if "fall_back_phone_number" in value:
        out["FallBackPhoneNumber"] = value["fall_back_phone_number"]
    if "phone_number_countries" in value:
        import aws_sdk_chime_sdk_voice.types.string_list

        out["PhoneNumberCountries"] = (
            aws_sdk_chime_sdk_voice.types.string_list.serialize_json(
                value["phone_number_countries"]
            )
        )
    return out


def deserialize_json(data: dict) -> Proxy:
    out: Proxy = {}  # type: ignore[typeddict-item]
    if "DefaultSessionExpiryMinutes" in data:
        out["default_session_expiry_minutes"] = data["DefaultSessionExpiryMinutes"]
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    if "FallBackPhoneNumber" in data:
        out["fall_back_phone_number"] = data["FallBackPhoneNumber"]
    if "PhoneNumberCountries" in data:
        import aws_sdk_chime_sdk_voice.types.string_list

        out["phone_number_countries"] = (
            aws_sdk_chime_sdk_voice.types.string_list.deserialize_json(
                data["PhoneNumberCountries"]
            )
        )
    return out
