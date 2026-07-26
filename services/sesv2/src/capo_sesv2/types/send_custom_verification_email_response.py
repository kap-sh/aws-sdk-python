"""Generated from Smithy shape ``com.amazonaws.sesv2#SendCustomVerificationEmailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.outbound_message_id


class SendCustomVerificationEmailResponse(TypedDict, closed=True):
    message_id: NotRequired["capo_sesv2.types.outbound_message_id.OutboundMessageId"]
    """<p>The unique message identifier returned from the <code>SendCustomVerificationEmail</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendCustomVerificationEmailResponse) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    return out


def deserialize_json(data: dict) -> SendCustomVerificationEmailResponse:
    out: SendCustomVerificationEmailResponse = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    return out
