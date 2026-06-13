"""Generated from Smithy shape ``com.amazonaws.wisdom#NotifyRecommendationsReceivedResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.notify_recommendations_received_error_list
    import aws_sdk_wisdom.types.recommendation_id_list


class NotifyRecommendationsReceivedResponse(TypedDict):
    recommendation_ids: NotRequired[
        "aws_sdk_wisdom.types.recommendation_id_list.RecommendationIdList"
    ]
    """<p>The identifiers of the recommendations.</p>"""
    errors: NotRequired[
        "aws_sdk_wisdom.types.notify_recommendations_received_error_list.NotifyRecommendationsReceivedErrorList"
    ]
    """<p>The identifiers of recommendations that are causing errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotifyRecommendationsReceivedResponse) -> dict:
    out: dict = {}
    if "recommendation_ids" in value:
        import aws_sdk_wisdom.types.recommendation_id_list

        out["recommendationIds"] = (
            aws_sdk_wisdom.types.recommendation_id_list.serialize_json(
                value["recommendation_ids"]
            )
        )
    if "errors" in value:
        import aws_sdk_wisdom.types.notify_recommendations_received_error_list

        out["errors"] = (
            aws_sdk_wisdom.types.notify_recommendations_received_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotifyRecommendationsReceivedResponse:
    out: NotifyRecommendationsReceivedResponse = {}  # type: ignore[typeddict-item]
    if "recommendationIds" in data:
        import aws_sdk_wisdom.types.recommendation_id_list

        out["recommendation_ids"] = (
            aws_sdk_wisdom.types.recommendation_id_list.deserialize_json(
                data["recommendationIds"]
            )
        )
    if "errors" in data:
        import aws_sdk_wisdom.types.notify_recommendations_received_error_list

        out["errors"] = (
            aws_sdk_wisdom.types.notify_recommendations_received_error_list.deserialize_json(
                data["errors"]
            )
        )
    return out
