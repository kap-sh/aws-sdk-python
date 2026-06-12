"""Generated from Smithy shape ``com.amazonaws.geoplaces#MatchScoreDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.component_match_scores
    import aws_sdk_geo_places.types.match_score


class MatchScoreDetails(TypedDict):
    overall: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>Indicates how well the entire input matches the returned. It is equal to 1 if all input tokens are recognized and matched.</p>"""
    components: NotRequired[
        "aws_sdk_geo_places.types.component_match_scores.ComponentMatchScores"
    ]
    """<p>Indicates how well the component input matches the returned. It is equal to 1 if all input tokens are recognized and matched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchScoreDetails) -> dict:
    out: dict = {}
    out["Overall"] = value.get("overall", 0)
    if "components" in value:
        import aws_sdk_geo_places.types.component_match_scores

        out["Components"] = (
            aws_sdk_geo_places.types.component_match_scores.serialize_json(
                value["components"]
            )
        )
    return out


def deserialize_json(data: dict) -> MatchScoreDetails:
    out: MatchScoreDetails = {}  # type: ignore[typeddict-item]
    if "Overall" in data:
        out["overall"] = data["Overall"]
    else:
        out["overall"] = 0
    if "Components" in data:
        import aws_sdk_geo_places.types.component_match_scores

        out["components"] = (
            aws_sdk_geo_places.types.component_match_scores.deserialize_json(
                data["Components"]
            )
        )
    return out
