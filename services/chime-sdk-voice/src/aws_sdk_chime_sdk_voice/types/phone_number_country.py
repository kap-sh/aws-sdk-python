"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberCountry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.alpha2_country_code
    import aws_sdk_chime_sdk_voice.types.phone_number_type_list


class PhoneNumberCountry(TypedDict):
    country_code: NotRequired[
        "aws_sdk_chime_sdk_voice.types.alpha2_country_code.Alpha2CountryCode"
    ]
    """<p>The phone number country code. Format: ISO 3166-1 alpha-2.</p>"""
    supported_phone_number_types: NotRequired[
        "aws_sdk_chime_sdk_voice.types.phone_number_type_list.PhoneNumberTypeList"
    ]
    """<p>The supported phone number types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberCountry) -> dict:
    out: dict = {}
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    if "supported_phone_number_types" in value:
        import aws_sdk_chime_sdk_voice.types.phone_number_type_list

        out["SupportedPhoneNumberTypes"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_type_list.serialize_json(
                value["supported_phone_number_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> PhoneNumberCountry:
    out: PhoneNumberCountry = {}  # type: ignore[typeddict-item]
    if "CountryCode" in data:
        out["country_code"] = data["CountryCode"]
    if "SupportedPhoneNumberTypes" in data:
        import aws_sdk_chime_sdk_voice.types.phone_number_type_list

        out["supported_phone_number_types"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_type_list.deserialize_json(
                data["SupportedPhoneNumberTypes"]
            )
        )
    return out
