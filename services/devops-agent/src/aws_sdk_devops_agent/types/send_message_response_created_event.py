"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageResponseCreatedEvent``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SendMessageResponseCreatedEvent(TypedDict):
    response_id: NotRequired["str"]
    """<p>The response ID</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageResponseCreatedEvent) -> dict:
    out: dict = {}
    if "response_id" in value:
        out["responseId"] = value["response_id"]
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageResponseCreatedEvent:
    out: SendMessageResponseCreatedEvent = {}  # type: ignore[typeddict-item]
    if "responseId" in data:
        out["response_id"] = data["responseId"]
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    return out
