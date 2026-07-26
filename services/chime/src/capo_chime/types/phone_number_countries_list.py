"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberCountriesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.phone_number_country

PhoneNumberCountriesList: TypeAlias = list[
    "capo_chime.types.phone_number_country.PhoneNumberCountry"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberCountriesList) -> list:
    import capo_chime.types.phone_number_country

    out: list = []
    for item in value:
        out.append(capo_chime.types.phone_number_country.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberCountriesList:
    import capo_chime.types.phone_number_country

    out: PhoneNumberCountriesList = []
    for item in data:
        out.append(capo_chime.types.phone_number_country.deserialize_json(item))
    return out
