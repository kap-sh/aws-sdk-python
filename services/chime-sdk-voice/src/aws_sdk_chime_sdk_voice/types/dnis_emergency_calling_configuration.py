"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DNISEmergencyCallingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.alpha2_country_code
    import aws_sdk_chime_sdk_voice.types.e164_phone_number


class DNISEmergencyCallingConfiguration(TypedDict, closed=True):
    emergency_phone_number: (
        "aws_sdk_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    )
    """<p>The DNIS phone number that you route emergency calls to, in E.164 format.</p>"""
    test_phone_number: NotRequired[
        "aws_sdk_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The DNIS phone number for routing test emergency calls to, in E.164 format.</p>"""
    calling_country: (
        "aws_sdk_chime_sdk_voice.types.alpha2_country_code.Alpha2CountryCode"
    )
    """<p>The country from which emergency calls are allowed, in ISO 3166-1 alpha-2 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DNISEmergencyCallingConfiguration) -> dict:
    out: dict = {}
    out["EmergencyPhoneNumber"] = value["emergency_phone_number"]
    if "test_phone_number" in value:
        out["TestPhoneNumber"] = value["test_phone_number"]
    out["CallingCountry"] = value["calling_country"]
    return out


def deserialize_json(data: dict) -> DNISEmergencyCallingConfiguration:
    out: DNISEmergencyCallingConfiguration = {}  # type: ignore[typeddict-item]
    if "EmergencyPhoneNumber" in data:
        out["emergency_phone_number"] = data["EmergencyPhoneNumber"]
    else:
        raise DeserializationError(
            "DNISEmergencyCallingConfiguration.emergency_phone_number required"
        )
    if "TestPhoneNumber" in data:
        out["test_phone_number"] = data["TestPhoneNumber"]
    if "CallingCountry" in data:
        out["calling_country"] = data["CallingCountry"]
    else:
        raise DeserializationError(
            "DNISEmergencyCallingConfiguration.calling_country required"
        )
    return out
