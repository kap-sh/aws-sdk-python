"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CarrierLookupResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.dialing_country_code_type
    import aws_sdk_pinpoint_sms_voice_v2.types.e164_phone_number_type
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code
    import aws_sdk_pinpoint_sms_voice_v2.types.mcc_type
    import aws_sdk_pinpoint_sms_voice_v2.types.mnc_type
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number_type

class CarrierLookupResult(TypedDict):
    e164_phone_number: "aws_sdk_pinpoint_sms_voice_v2.types.e164_phone_number_type.E164PhoneNumberType"
    """<p>The phone number in E164 format, sanitized from the original input by removing any formatting characters.</p>"""
    dialing_country_code: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.dialing_country_code_type.DialingCountryCodeType"]
    """<p>The country or region numeric dialing code for the phone number.</p>"""
    iso_country_code: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code.IsoCountryCode"]
    """<p>The two-character country or region code, in ISO 3166-1 alpha-2 format, for the phone number.</p>"""
    country: NotRequired["str"]
    """<p>The name of the country or region for the phone number.</p>"""
    mcc: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.mcc_type.MCCType"]
    """<p>The phone number's mobile country code, for mobile phone number types</p>"""
    mnc: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.mnc_type.MNCType"]
    """<p>The phone number's mobile network code, for mobile phone number types.</p>"""
    carrier: NotRequired["str"]
    """<p>The carrier or service provider that the phone number is currently registered with. In some countries and regions, this value may be the carrier or service provider that the phone number was originally registered with.</p>"""
    phone_number_type: "aws_sdk_pinpoint_sms_voice_v2.types.phone_number_type.PhoneNumberType"
    """<p>Describes the type of phone number. Valid values are: MOBILE, LANDLINE, OTHER, and INVALID. Avoid sending SMS or voice messages to INVALID phone numbers, as these numbers are unlikely to belong to actual recipients.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CarrierLookupResult) -> dict:
    out: dict = {}
    out["E164PhoneNumber"] = value["e164_phone_number"]
    if "dialing_country_code" in value:
        out["DialingCountryCode"] = value["dialing_country_code"]
    if "iso_country_code" in value:
        out["IsoCountryCode"] = value["iso_country_code"]
    if "country" in value:
        out["Country"] = value["country"]
    if "mcc" in value:
        out["MCC"] = value["mcc"]
    if "mnc" in value:
        out["MNC"] = value["mnc"]
    if "carrier" in value:
        out["Carrier"] = value["carrier"]
    out["PhoneNumberType"] = value["phone_number_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CarrierLookupResult:
    out: CarrierLookupResult = {}  # type: ignore[typeddict-item]
    if "E164PhoneNumber" in data:
        out["e164_phone_number"] = data["E164PhoneNumber"]
    else:
        raise DeserializationError("CarrierLookupResult.e164_phone_number required")
    if "DialingCountryCode" in data:
        out["dialing_country_code"] = data["DialingCountryCode"]
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    if "Country" in data:
        out["country"] = data["Country"]
    if "MCC" in data:
        out["mcc"] = data["MCC"]
    if "MNC" in data:
        out["mnc"] = data["MNC"]
    if "Carrier" in data:
        out["carrier"] = data["Carrier"]
    if "PhoneNumberType" in data:
        out["phone_number_type"] = data["PhoneNumberType"]
    else:
        raise DeserializationError("CarrierLookupResult.phone_number_type required")
    return out