"""Generated from Smithy shape ``com.amazonaws.pinpoint#NumberValidateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class NumberValidateRequest(TypedDict):
    iso_country_code: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region where the phone number was originally registered.</p>"""
    phone_number: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The phone number to retrieve information about. The phone number that you provide should include a valid numeric country code. Otherwise, the operation might result in an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberValidateRequest) -> dict:
    out: dict = {}
    if "iso_country_code" in value:
        out["IsoCountryCode"] = value["iso_country_code"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    return out


def deserialize_json(data: dict) -> NumberValidateRequest:
    out: NumberValidateRequest = {}  # type: ignore[typeddict-item]
    if "IsoCountryCode" in data:
        out["iso_country_code"] = data["IsoCountryCode"]
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    return out
