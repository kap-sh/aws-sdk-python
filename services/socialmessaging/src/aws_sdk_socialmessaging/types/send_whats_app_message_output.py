"""Generated from Smithy shape ``com.amazonaws.socialmessaging#SendWhatsAppMessageOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SendWhatsAppMessageOutput(TypedDict):
    message_id: NotRequired["str"]
    """<p>The unique identifier of the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendWhatsAppMessageOutput) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["messageId"] = value["message_id"]
    return out


def deserialize_json(data: dict) -> SendWhatsAppMessageOutput:
    out: SendWhatsAppMessageOutput = {}  # type: ignore[typeddict-item]
    if "messageId" in data:
        out["message_id"] = data["messageId"]
    return out
