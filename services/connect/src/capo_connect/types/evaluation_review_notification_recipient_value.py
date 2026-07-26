"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewNotificationRecipientValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.resource_id


class EvaluationReviewNotificationRecipientValue(TypedDict, closed=True):
    user_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The user identifier for the notification recipient.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewNotificationRecipientValue) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> EvaluationReviewNotificationRecipientValue:
    out: EvaluationReviewNotificationRecipientValue = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    return out
