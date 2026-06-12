"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#GetPersonalizedRankingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.item_list
    import aws_sdk_personalize_runtime.types.recommendation_id


class GetPersonalizedRankingResponse(TypedDict):
    personalized_ranking: NotRequired[
        "aws_sdk_personalize_runtime.types.item_list.ItemList"
    ]
    """<p>A list of items in order of most likely interest to the user. The maximum is 500.</p>"""
    recommendation_id: NotRequired[
        "aws_sdk_personalize_runtime.types.recommendation_id.RecommendationID"
    ]
    """<p>The ID of the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPersonalizedRankingResponse) -> dict:
    out: dict = {}
    if "personalized_ranking" in value:
        import aws_sdk_personalize_runtime.types.item_list

        out["personalizedRanking"] = (
            aws_sdk_personalize_runtime.types.item_list.serialize_json(
                value["personalized_ranking"]
            )
        )
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    return out


def deserialize_json(data: dict) -> GetPersonalizedRankingResponse:
    out: GetPersonalizedRankingResponse = {}  # type: ignore[typeddict-item]
    if "personalizedRanking" in data:
        import aws_sdk_personalize_runtime.types.item_list

        out["personalized_ranking"] = (
            aws_sdk_personalize_runtime.types.item_list.deserialize_json(
                data["personalizedRanking"]
            )
        )
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    return out
