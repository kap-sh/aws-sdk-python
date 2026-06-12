"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#GetActionRecommendationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.action_list
    import aws_sdk_personalize_runtime.types.recommendation_id


class GetActionRecommendationsResponse(TypedDict):
    action_list: NotRequired["aws_sdk_personalize_runtime.types.action_list.ActionList"]
    """<p>A list of action recommendations sorted in descending order by prediction score. There can be a maximum of 100 actions in the list. For information about action scores, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/how-action-recommendation-scoring-works.html\">How action recommendation scoring works</a>.</p>"""
    recommendation_id: NotRequired[
        "aws_sdk_personalize_runtime.types.recommendation_id.RecommendationID"
    ]
    """<p>The ID of the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetActionRecommendationsResponse) -> dict:
    out: dict = {}
    if "action_list" in value:
        import aws_sdk_personalize_runtime.types.action_list

        out["actionList"] = (
            aws_sdk_personalize_runtime.types.action_list.serialize_json(
                value["action_list"]
            )
        )
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    return out


def deserialize_json(data: dict) -> GetActionRecommendationsResponse:
    out: GetActionRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "actionList" in data:
        import aws_sdk_personalize_runtime.types.action_list

        out["action_list"] = (
            aws_sdk_personalize_runtime.types.action_list.deserialize_json(
                data["actionList"]
            )
        )
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    return out
