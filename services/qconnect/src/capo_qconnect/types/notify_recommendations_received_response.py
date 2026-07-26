"""Generated from Smithy shape ``com.amazonaws.qconnect#NotifyRecommendationsReceivedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.notify_recommendations_received_error_list
    import capo_qconnect.types.recommendation_id_list


class NotifyRecommendationsReceivedResponse(TypedDict, closed=True):
    recommendation_ids: NotRequired[
        "capo_qconnect.types.recommendation_id_list.RecommendationIdList"
    ]
    """<p>The identifiers of the recommendations.</p>"""
    errors: NotRequired[
        "capo_qconnect.types.notify_recommendations_received_error_list.NotifyRecommendationsReceivedErrorList"
    ]
    """<p>The identifiers of recommendations that are causing errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotifyRecommendationsReceivedResponse) -> dict:
    out: dict = {}
    if "recommendation_ids" in value:
        import capo_qconnect.types.recommendation_id_list

        out["recommendationIds"] = (
            capo_qconnect.types.recommendation_id_list.serialize_json(
                value["recommendation_ids"]
            )
        )
    if "errors" in value:
        import capo_qconnect.types.notify_recommendations_received_error_list

        out["errors"] = (
            capo_qconnect.types.notify_recommendations_received_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotifyRecommendationsReceivedResponse:
    out: NotifyRecommendationsReceivedResponse = {}  # type: ignore[typeddict-item]
    if "recommendationIds" in data:
        import capo_qconnect.types.recommendation_id_list

        out["recommendation_ids"] = (
            capo_qconnect.types.recommendation_id_list.deserialize_json(
                data["recommendationIds"]
            )
        )
    if "errors" in data:
        import capo_qconnect.types.notify_recommendations_received_error_list

        out["errors"] = (
            capo_qconnect.types.notify_recommendations_received_error_list.deserialize_json(
                data["errors"]
            )
        )
    return out
