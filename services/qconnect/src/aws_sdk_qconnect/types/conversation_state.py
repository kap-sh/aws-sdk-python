"""Generated from Smithy shape ``com.amazonaws.qconnect#ConversationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.conversation_status
    import aws_sdk_qconnect.types.conversation_status_reason


class ConversationState(TypedDict, closed=True):
    status: "aws_sdk_qconnect.types.conversation_status.ConversationStatus"
    """<p>The status of the conversation state.</p>"""
    reason: NotRequired[
        "aws_sdk_qconnect.types.conversation_status_reason.ConversationStatusReason"
    ]
    """<p>The reason of the conversation state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationState) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ConversationState:
    out: ConversationState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ConversationState.status required")
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
