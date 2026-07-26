"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressedDestinationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.feedback_id
    import capo_sesv2.types.outbound_message_id


class SuppressedDestinationAttributes(TypedDict, closed=True):
    message_id: NotRequired["capo_sesv2.types.outbound_message_id.OutboundMessageId"]
    """<p>The unique identifier of the email message that caused the email address to be added to the suppression list for your account or for a specific tenant.</p>"""
    feedback_id: NotRequired["capo_sesv2.types.feedback_id.FeedbackId"]
    """<p>A unique identifier that's generated when an email address is added to the suppression list for your account or for a specific tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressedDestinationAttributes) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "feedback_id" in value:
        out["FeedbackId"] = value["feedback_id"]
    return out


def deserialize_json(data: dict) -> SuppressedDestinationAttributes:
    out: SuppressedDestinationAttributes = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    if "FeedbackId" in data:
        out["feedback_id"] = data["FeedbackId"]
    return out
