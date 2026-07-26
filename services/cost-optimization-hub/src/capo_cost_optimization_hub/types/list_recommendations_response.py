"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ListRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.recommendation_list


class ListRecommendationsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_cost_optimization_hub.types.recommendation_list.RecommendationList"
    ]
    """<p>List of all savings recommendations.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendationsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_cost_optimization_hub.types.recommendation_list

        out["items"] = (
            capo_cost_optimization_hub.types.recommendation_list.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendationsResponse:
    out: ListRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_cost_optimization_hub.types.recommendation_list

        out["items"] = (
            capo_cost_optimization_hub.types.recommendation_list.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
