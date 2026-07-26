"""Generated from Smithy shape ``com.amazonaws.sesv2#SendEmailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.outbound_message_id


class SendEmailResponse(TypedDict, closed=True):
    message_id: NotRequired["capo_sesv2.types.outbound_message_id.OutboundMessageId"]
    """<p>A unique identifier for the message that is generated when the message is accepted.</p> <note> <p>It's possible for Amazon SES to accept a message without sending it. For example, this can happen when the message that you're trying to send has an attachment that contains a virus, or when you send a templated email that contains invalid personalization content.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendEmailResponse) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    return out


def deserialize_json(data: dict) -> SendEmailResponse:
    out: SendEmailResponse = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    return out
