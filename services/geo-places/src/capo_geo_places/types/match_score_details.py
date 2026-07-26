"""Generated from Smithy shape ``com.amazonaws.geoplaces#MatchScoreDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.component_match_scores
    import capo_geo_places.types.match_score


class MatchScoreDetails(TypedDict, closed=True):
    overall: "capo_geo_places.types.match_score.MatchScore"
    """<p>Indicates how well the entire input matches the returned. It is equal to 1 if all input tokens are recognized and matched.</p>"""
    components: NotRequired[
        "capo_geo_places.types.component_match_scores.ComponentMatchScores"
    ]
    """<p>Indicates how well the component input matches the returned. It is equal to 1 if all input tokens are recognized and matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchScoreDetails) -> dict:
    out: dict = {}
    out["Overall"] = value.get("overall", 0)
    if "components" in value:
        import capo_geo_places.types.component_match_scores

        out["Components"] = capo_geo_places.types.component_match_scores.serialize_json(
            value["components"]
        )
    return out


def deserialize_json(data: dict) -> MatchScoreDetails:
    out: MatchScoreDetails = {}  # type: ignore[typeddict-item]
    if "Overall" in data:
        out["overall"] = data["Overall"]
    else:
        out["overall"] = 0
    if "Components" in data:
        import capo_geo_places.types.component_match_scores

        out["components"] = (
            capo_geo_places.types.component_match_scores.deserialize_json(
                data["Components"]
            )
        )
    return out
