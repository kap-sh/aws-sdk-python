"""Generated from Smithy shape ``com.amazonaws.geoplaces#CountryHighlights``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.highlight_list


class CountryHighlights(TypedDict):
    code: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending index of the country code in the text query that match the found title.</p>"""
    name: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending index of the country code in the text query that match the found title.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CountryHighlights) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["Code"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["code"]
        )
    if "name" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["Name"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["name"]
        )
    return out


def deserialize_json(data: dict) -> CountryHighlights:
    out: CountryHighlights = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["code"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["Code"]
        )
    if "Name" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["name"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["Name"]
        )
    return out
