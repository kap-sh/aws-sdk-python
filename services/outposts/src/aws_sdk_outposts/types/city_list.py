"""Generated from Smithy shape ``com.amazonaws.outposts#CityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.city

CityList: TypeAlias = list["aws_sdk_outposts.types.city.City"]


# --- restJson1 ser/de ---
def serialize_json(value: CityList) -> list:
    return list(value)


def deserialize_json(data: list) -> CityList:
    return list(data)
