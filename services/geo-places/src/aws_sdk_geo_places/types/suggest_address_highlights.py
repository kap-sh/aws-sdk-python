"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestAddressHighlights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.highlight_list


class SuggestAddressHighlights(TypedDict, closed=True):
    label: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending indexes of the places in the result which were identified to match the textQuery. This result is useful for providing emphasis to results where the user query directly matched to make selecting the correct result from a list easier for an end user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestAddressHighlights) -> dict:
    out: dict = {}
    if "label" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["Label"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["label"]
        )
    return out


def deserialize_json(data: dict) -> SuggestAddressHighlights:
    out: SuggestAddressHighlights = {}  # type: ignore[typeddict-item]
    if "Label" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["label"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["Label"]
        )
    return out
