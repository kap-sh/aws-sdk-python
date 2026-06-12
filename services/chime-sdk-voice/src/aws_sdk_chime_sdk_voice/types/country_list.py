"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CountryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.country

CountryList: TypeAlias = list["aws_sdk_chime_sdk_voice.types.country.Country"]


# --- restJson1 ser/de ---
def serialize_json(value: CountryList) -> list:
    return list(value)


def deserialize_json(data: list) -> CountryList:
    return list(data)
