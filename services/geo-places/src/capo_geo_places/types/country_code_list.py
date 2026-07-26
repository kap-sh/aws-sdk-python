"""Generated from Smithy shape ``com.amazonaws.geoplaces#CountryCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.country_code

CountryCodeList: TypeAlias = list["capo_geo_places.types.country_code.CountryCode"]


# --- restJson1 ser/de ---
def serialize_json(value: CountryCodeList) -> list:
    return list(value)


def deserialize_json(data: list) -> CountryCodeList:
    return list(data)
