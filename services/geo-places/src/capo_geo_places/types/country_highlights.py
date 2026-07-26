"""Generated from Smithy shape ``com.amazonaws.geoplaces#CountryHighlights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.highlight_list


class CountryHighlights(TypedDict, closed=True):
    code: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending index of the country code in the text query that match the found title.</p>"""
    name: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending index of the country code in the text query that match the found title.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CountryHighlights) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_geo_places.types.highlight_list

        out["Code"] = capo_geo_places.types.highlight_list.serialize_json(value["code"])
    if "name" in value:
        import capo_geo_places.types.highlight_list

        out["Name"] = capo_geo_places.types.highlight_list.serialize_json(value["name"])
    return out


def deserialize_json(data: dict) -> CountryHighlights:
    out: CountryHighlights = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_geo_places.types.highlight_list

        out["code"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Code"]
        )
    if "Name" in data:
        import capo_geo_places.types.highlight_list

        out["name"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Name"]
        )
    return out
