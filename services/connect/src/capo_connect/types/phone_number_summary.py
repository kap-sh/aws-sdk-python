"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.phone_number
    import capo_connect.types.phone_number_country_code
    import capo_connect.types.phone_number_id
    import capo_connect.types.phone_number_type


class PhoneNumberSummary(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.phone_number_id.PhoneNumberId"]
    """<p>The identifier of the phone number.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the phone number.</p>"""
    phone_number: NotRequired["capo_connect.types.phone_number.PhoneNumber"]
    """<p>The phone number.</p>"""
    phone_number_type: NotRequired[
        "capo_connect.types.phone_number_type.PhoneNumberType"
    ]
    """<p>The type of phone number.</p>"""
    phone_number_country_code: NotRequired[
        "capo_connect.types.phone_number_country_code.PhoneNumberCountryCode"
    ]
    """<p>The ISO country code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "phone_number_type" in value:
        import capo_connect.types.phone_number_type

        out["PhoneNumberType"] = capo_connect.types.phone_number_type.serialize_json(
            value["phone_number_type"]
        )
    if "phone_number_country_code" in value:
        import capo_connect.types.phone_number_country_code

        out["PhoneNumberCountryCode"] = (
            capo_connect.types.phone_number_country_code.serialize_json(
                value["phone_number_country_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> PhoneNumberSummary:
    out: PhoneNumberSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    if "PhoneNumberType" in data:
        import capo_connect.types.phone_number_type

        out["phone_number_type"] = (
            capo_connect.types.phone_number_type.deserialize_json(
                data["PhoneNumberType"]
            )
        )
    if "PhoneNumberCountryCode" in data:
        import capo_connect.types.phone_number_country_code

        out["phone_number_country_code"] = (
            capo_connect.types.phone_number_country_code.deserialize_json(
                data["PhoneNumberCountryCode"]
            )
        )
    return out
