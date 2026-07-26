"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberCountryCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.phone_number_country_code

PhoneNumberCountryCodes: TypeAlias = list[
    "capo_connect.types.phone_number_country_code.PhoneNumberCountryCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberCountryCodes) -> list:
    import capo_connect.types.phone_number_country_code

    out: list = []
    for item in value:
        out.append(capo_connect.types.phone_number_country_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberCountryCodes:
    import capo_connect.types.phone_number_country_code

    out: PhoneNumberCountryCodes = []
    for item in data:
        out.append(capo_connect.types.phone_number_country_code.deserialize_json(item))
    return out
