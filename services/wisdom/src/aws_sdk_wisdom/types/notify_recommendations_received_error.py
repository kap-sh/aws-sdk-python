"""Generated from Smithy shape ``com.amazonaws.wisdom#NotifyRecommendationsReceivedError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.notify_recommendations_received_error_message


class NotifyRecommendationsReceivedError(TypedDict, closed=True):
    recommendation_id: NotRequired["str"]
    """<p>The identifier of the recommendation that is in error.</p>"""
    message: NotRequired[
        "aws_sdk_wisdom.types.notify_recommendations_received_error_message.NotifyRecommendationsReceivedErrorMessage"
    ]
    """<p>A recommendation is causing an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotifyRecommendationsReceivedError) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotifyRecommendationsReceivedError:
    out: NotifyRecommendationsReceivedError = {}  # type: ignore[typeddict-item]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    if "message" in data:
        out["message"] = data["message"]
    return out
