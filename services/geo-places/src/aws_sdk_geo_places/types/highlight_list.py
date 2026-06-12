"""Generated from Smithy shape ``com.amazonaws.geoplaces#HighlightList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.highlight

HighlightList: TypeAlias = list["aws_sdk_geo_places.types.highlight.Highlight"]


# --- restJson1 ser/de ---
def serialize_json(value: HighlightList) -> list:
    import aws_sdk_geo_places.types.highlight

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_places.types.highlight.serialize_json(item))
    return out


def deserialize_json(data: list) -> HighlightList:
    import aws_sdk_geo_places.types.highlight

    out: HighlightList = []
    for item in data:
        out.append(aws_sdk_geo_places.types.highlight.deserialize_json(item))
    return out
