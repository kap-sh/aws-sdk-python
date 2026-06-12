"""Generated from Smithy shape ``com.amazonaws.pinpointemail#SendEmailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.outbound_message_id


class SendEmailResponse(TypedDict):
    message_id: NotRequired[
        "aws_sdk_pinpoint_email.types.outbound_message_id.OutboundMessageId"
    ]
    """<p>A unique identifier for the message that is generated when Amazon Pinpoint accepts the message.</p> <note> <p>It is possible for Amazon Pinpoint to accept a message without sending it. This can happen when the message you're trying to send has an attachment doesn't pass a virus check, or when you send a templated email that contains invalid personalization content, for example.</p> </note>"""


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
