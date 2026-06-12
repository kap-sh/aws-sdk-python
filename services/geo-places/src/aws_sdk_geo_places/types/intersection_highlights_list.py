"""Generated from Smithy shape ``com.amazonaws.geoplaces#IntersectionHighlightsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.highlight_list

IntersectionHighlightsList: TypeAlias = list[
    "aws_sdk_geo_places.types.highlight_list.HighlightList"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntersectionHighlightsList) -> list:
    import aws_sdk_geo_places.types.highlight_list

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_places.types.highlight_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntersectionHighlightsList:
    import aws_sdk_geo_places.types.highlight_list

    out: IntersectionHighlightsList = []
    for item in data:
        out.append(aws_sdk_geo_places.types.highlight_list.deserialize_json(item))
    return out
