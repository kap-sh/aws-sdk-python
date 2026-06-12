"""Generated from Smithy shape ``com.amazonaws.outposts#CountryCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.country_code

CountryCodeList: TypeAlias = list["aws_sdk_outposts.types.country_code.CountryCode"]


# --- restJson1 ser/de ---
def serialize_json(value: CountryCodeList) -> list:
    return list(value)


def deserialize_json(data: list) -> CountryCodeList:
    return list(data)
