"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberCountry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.alpha2_country_code
    import capo_chime.types.phone_number_type_list


class PhoneNumberCountry(TypedDict, closed=True):
    country_code: NotRequired["capo_chime.types.alpha2_country_code.Alpha2CountryCode"]
    """<p>The phone number country code. Format: ISO 3166-1 alpha-2.</p>"""
    supported_phone_number_types: NotRequired[
        "capo_chime.types.phone_number_type_list.PhoneNumberTypeList"
    ]
    """<p>The supported phone number types. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberCountry) -> dict:
    out: dict = {}
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    if "supported_phone_number_types" in value:
        import capo_chime.types.phone_number_type_list

        out["SupportedPhoneNumberTypes"] = (
            capo_chime.types.phone_number_type_list.serialize_json(
                value["supported_phone_number_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> PhoneNumberCountry:
    out: PhoneNumberCountry = {}  # type: ignore[typeddict-item]
    if "CountryCode" in data:
        out["country_code"] = data["CountryCode"]
    if "SupportedPhoneNumberTypes" in data:
        import capo_chime.types.phone_number_type_list

        out["supported_phone_number_types"] = (
            capo_chime.types.phone_number_type_list.deserialize_json(
                data["SupportedPhoneNumberTypes"]
            )
        )
    return out
