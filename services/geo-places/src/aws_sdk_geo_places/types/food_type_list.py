"""Generated from Smithy shape ``com.amazonaws.geoplaces#FoodTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.food_type

FoodTypeList: TypeAlias = list["aws_sdk_geo_places.types.food_type.FoodType"]


# --- restJson1 ser/de ---
def serialize_json(value: FoodTypeList) -> list:
    import aws_sdk_geo_places.types.food_type

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_places.types.food_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> FoodTypeList:
    import aws_sdk_geo_places.types.food_type

    out: FoodTypeList = []
    for item in data:
        out.append(aws_sdk_geo_places.types.food_type.deserialize_json(item))
    return out
