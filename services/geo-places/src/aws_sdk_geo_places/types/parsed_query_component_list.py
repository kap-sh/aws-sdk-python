"""Generated from Smithy shape ``com.amazonaws.geoplaces#ParsedQueryComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.parsed_query_component

ParsedQueryComponentList: TypeAlias = list[
    "aws_sdk_geo_places.types.parsed_query_component.ParsedQueryComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParsedQueryComponentList) -> list:
    import aws_sdk_geo_places.types.parsed_query_component

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_places.types.parsed_query_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParsedQueryComponentList:
    import aws_sdk_geo_places.types.parsed_query_component

    out: ParsedQueryComponentList = []
    for item in data:
        out.append(
            aws_sdk_geo_places.types.parsed_query_component.deserialize_json(item)
        )
    return out
