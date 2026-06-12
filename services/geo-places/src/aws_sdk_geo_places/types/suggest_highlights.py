"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestHighlights``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.highlight_list
    import aws_sdk_geo_places.types.suggest_address_highlights


class SuggestHighlights(TypedDict):
    title: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending index of the title in the text query that match the found title. </p>"""
    address: NotRequired[
        "aws_sdk_geo_places.types.suggest_address_highlights.SuggestAddressHighlights"
    ]
    """<p>The place's address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestHighlights) -> dict:
    out: dict = {}
    if "title" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["Title"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["title"]
        )
    if "address" in value:
        import aws_sdk_geo_places.types.suggest_address_highlights

        out["Address"] = (
            aws_sdk_geo_places.types.suggest_address_highlights.serialize_json(
                value["address"]
            )
        )
    return out


def deserialize_json(data: dict) -> SuggestHighlights:
    out: SuggestHighlights = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["title"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["Title"]
        )
    if "Address" in data:
        import aws_sdk_geo_places.types.suggest_address_highlights

        out["address"] = (
            aws_sdk_geo_places.types.suggest_address_highlights.deserialize_json(
                data["Address"]
            )
        )
    return out
