"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MessageMetadata``."""

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError


class MessageMetadata(TypedDict, closed=True):
    event_id: "str"
    """<p>The identifier of the event associated with this message.</p>"""
    message_index: "int"
    """<p>The position of this message within that event’s ordered list of messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageMetadata) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["messageIndex"] = value["message_index"]
    return out


def deserialize_json(data: dict) -> MessageMetadata:
    out: MessageMetadata = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("MessageMetadata.event_id required")
    if data.get("messageIndex") is not None:
        out["message_index"] = data["messageIndex"]
    else:
        raise DeserializationError("MessageMetadata.message_index required")
    return out
