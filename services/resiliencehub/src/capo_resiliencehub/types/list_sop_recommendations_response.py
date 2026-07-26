"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListSopRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.sop_recommendation_list


class ListSopRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""
    sop_recommendations: (
        "capo_resiliencehub.types.sop_recommendation_list.SopRecommendationList"
    )
    """<p>The standard operating procedure (SOP) recommendations for the Resilience Hub applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSopRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_resiliencehub.types.sop_recommendation_list

    out["sopRecommendations"] = (
        capo_resiliencehub.types.sop_recommendation_list.serialize_json(
            value["sop_recommendations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListSopRecommendationsResponse:
    out: ListSopRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sopRecommendations" in data:
        import capo_resiliencehub.types.sop_recommendation_list

        out["sop_recommendations"] = (
            capo_resiliencehub.types.sop_recommendation_list.deserialize_json(
                data["sopRecommendations"]
            )
        )
    else:
        raise DeserializationError(
            "ListSopRecommendationsResponse.sop_recommendations required"
        )
    return out
