"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#GetRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.item_list
    import aws_sdk_personalize_runtime.types.recommendation_id


class GetRecommendationsResponse(TypedDict, closed=True):
    item_list: NotRequired["aws_sdk_personalize_runtime.types.item_list.ItemList"]
    """<p>A list of recommendations sorted in descending order by prediction score. There can be a maximum of 500 items in the list.</p>"""
    recommendation_id: NotRequired[
        "aws_sdk_personalize_runtime.types.recommendation_id.RecommendationID"
    ]
    """<p>The ID of the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationsResponse) -> dict:
    out: dict = {}
    if "item_list" in value:
        import aws_sdk_personalize_runtime.types.item_list

        out["itemList"] = aws_sdk_personalize_runtime.types.item_list.serialize_json(
            value["item_list"]
        )
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    return out


def deserialize_json(data: dict) -> GetRecommendationsResponse:
    out: GetRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "itemList" in data:
        import aws_sdk_personalize_runtime.types.item_list

        out["item_list"] = aws_sdk_personalize_runtime.types.item_list.deserialize_json(
            data["itemList"]
        )
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    return out
