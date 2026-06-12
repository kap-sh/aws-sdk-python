"""Generated from Smithy shape ``com.amazonaws.connect#AvailableNumberSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.phone_number
    import aws_sdk_connect.types.phone_number_country_code
    import aws_sdk_connect.types.phone_number_type


class AvailableNumberSummary(TypedDict):
    phone_number: NotRequired["aws_sdk_connect.types.phone_number.PhoneNumber"]
    """<p>The phone number. Phone numbers are formatted <code>[+] [country code] [subscriber number including area code]</code>.</p>"""
    phone_number_country_code: NotRequired[
        "aws_sdk_connect.types.phone_number_country_code.PhoneNumberCountryCode"
    ]
    """<p>The ISO country code.</p>"""
    phone_number_type: NotRequired[
        "aws_sdk_connect.types.phone_number_type.PhoneNumberType"
    ]
    """<p>The type of phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailableNumberSummary) -> dict:
    out: dict = {}
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "phone_number_country_code" in value:
        import aws_sdk_connect.types.phone_number_country_code

        out["PhoneNumberCountryCode"] = (
            aws_sdk_connect.types.phone_number_country_code.serialize_json(
                value["phone_number_country_code"]
            )
        )
    if "phone_number_type" in value:
        import aws_sdk_connect.types.phone_number_type

        out["PhoneNumberType"] = aws_sdk_connect.types.phone_number_type.serialize_json(
            value["phone_number_type"]
        )
    return out


def deserialize_json(data: dict) -> AvailableNumberSummary:
    out: AvailableNumberSummary = {}  # type: ignore[typeddict-item]
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    if "PhoneNumberCountryCode" in data:
        import aws_sdk_connect.types.phone_number_country_code

        out["phone_number_country_code"] = (
            aws_sdk_connect.types.phone_number_country_code.deserialize_json(
                data["PhoneNumberCountryCode"]
            )
        )
    if "PhoneNumberType" in data:
        import aws_sdk_connect.types.phone_number_type

        out["phone_number_type"] = (
            aws_sdk_connect.types.phone_number_type.deserialize_json(
                data["PhoneNumberType"]
            )
        )
    return out
