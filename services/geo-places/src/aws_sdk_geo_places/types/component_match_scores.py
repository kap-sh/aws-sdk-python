"""Generated from Smithy shape ``com.amazonaws.geoplaces#ComponentMatchScores``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.address_component_match_scores
    import aws_sdk_geo_places.types.match_score


class ComponentMatchScores(TypedDict, closed=True):
    title: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>Indicates the match score of the title in the text query that match the found title. </p>"""
    address: NotRequired[
        "aws_sdk_geo_places.types.address_component_match_scores.AddressComponentMatchScores"
    ]
    """<p>The place's address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentMatchScores) -> dict:
    out: dict = {}
    out["Title"] = value.get("title", 0)
    if "address" in value:
        import aws_sdk_geo_places.types.address_component_match_scores

        out["Address"] = (
            aws_sdk_geo_places.types.address_component_match_scores.serialize_json(
                value["address"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentMatchScores:
    out: ComponentMatchScores = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        out["title"] = 0
    if "Address" in data:
        import aws_sdk_geo_places.types.address_component_match_scores

        out["address"] = (
            aws_sdk_geo_places.types.address_component_match_scores.deserialize_json(
                data["Address"]
            )
        )
    return out
