"""Generated from Smithy shape ``com.amazonaws.location#CountryCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.country_code3

CountryCodeList: TypeAlias = list["capo_location.types.country_code3.CountryCode3"]


# --- restJson1 ser/de ---
def serialize_json(value: CountryCodeList) -> list:
    return list(value)


def deserialize_json(data: list) -> CountryCodeList:
    return list(data)
