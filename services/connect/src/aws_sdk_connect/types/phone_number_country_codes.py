"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberCountryCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.phone_number_country_code

PhoneNumberCountryCodes: TypeAlias = list[
    "aws_sdk_connect.types.phone_number_country_code.PhoneNumberCountryCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberCountryCodes) -> list:
    import aws_sdk_connect.types.phone_number_country_code

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.phone_number_country_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberCountryCodes:
    import aws_sdk_connect.types.phone_number_country_code

    out: PhoneNumberCountryCodes = []
    for item in data:
        out.append(
            aws_sdk_connect.types.phone_number_country_code.deserialize_json(item)
        )
    return out
