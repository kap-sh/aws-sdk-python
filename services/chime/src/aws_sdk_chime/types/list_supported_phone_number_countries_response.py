"""Generated from Smithy shape ``com.amazonaws.chime#ListSupportedPhoneNumberCountriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.phone_number_countries_list


class ListSupportedPhoneNumberCountriesResponse(TypedDict, closed=True):
    phone_number_countries: NotRequired[
        "aws_sdk_chime.types.phone_number_countries_list.PhoneNumberCountriesList"
    ]
    """<p>The supported phone number countries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSupportedPhoneNumberCountriesResponse) -> dict:
    out: dict = {}
    if "phone_number_countries" in value:
        import aws_sdk_chime.types.phone_number_countries_list

        out["PhoneNumberCountries"] = (
            aws_sdk_chime.types.phone_number_countries_list.serialize_json(
                value["phone_number_countries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSupportedPhoneNumberCountriesResponse:
    out: ListSupportedPhoneNumberCountriesResponse = {}  # type: ignore[typeddict-item]
    if "PhoneNumberCountries" in data:
        import aws_sdk_chime.types.phone_number_countries_list

        out["phone_number_countries"] = (
            aws_sdk_chime.types.phone_number_countries_list.deserialize_json(
                data["PhoneNumberCountries"]
            )
        )
    return out
