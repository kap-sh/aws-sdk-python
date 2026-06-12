"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.reverse_geocode_result_item

ReverseGeocodeResultItemList: TypeAlias = list[
    "aws_sdk_geo_places.types.reverse_geocode_result_item.ReverseGeocodeResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeResultItemList) -> list:
    import aws_sdk_geo_places.types.reverse_geocode_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_places.types.reverse_geocode_result_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReverseGeocodeResultItemList:
    import aws_sdk_geo_places.types.reverse_geocode_result_item

    out: ReverseGeocodeResultItemList = []
    for item in data:
        out.append(
            aws_sdk_geo_places.types.reverse_geocode_result_item.deserialize_json(item)
        )
    return out
