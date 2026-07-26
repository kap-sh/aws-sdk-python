"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteHighlights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.autocomplete_address_highlights
    import capo_geo_places.types.highlight_list


class AutocompleteHighlights(TypedDict, closed=True):
    title: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates where the title field in the result matches the input query.</p>"""
    address: NotRequired[
        "capo_geo_places.types.autocomplete_address_highlights.AutocompleteAddressHighlights"
    ]
    """<p>Describes how part of the result address match the input query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteHighlights) -> dict:
    out: dict = {}
    if "title" in value:
        import capo_geo_places.types.highlight_list

        out["Title"] = capo_geo_places.types.highlight_list.serialize_json(
            value["title"]
        )
    if "address" in value:
        import capo_geo_places.types.autocomplete_address_highlights

        out["Address"] = (
            capo_geo_places.types.autocomplete_address_highlights.serialize_json(
                value["address"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutocompleteHighlights:
    out: AutocompleteHighlights = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        import capo_geo_places.types.highlight_list

        out["title"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Title"]
        )
    if "Address" in data:
        import capo_geo_places.types.autocomplete_address_highlights

        out["address"] = (
            capo_geo_places.types.autocomplete_address_highlights.deserialize_json(
                data["Address"]
            )
        )
    return out
