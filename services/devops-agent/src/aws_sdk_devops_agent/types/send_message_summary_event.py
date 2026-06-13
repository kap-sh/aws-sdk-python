"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageSummaryEvent``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SendMessageSummaryEvent(TypedDict):
    content: NotRequired["str"]
    """<p>Summary content</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageSummaryEvent) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageSummaryEvent:
    out: SendMessageSummaryEvent = {}  # type: ignore[typeddict-item]
    if "content" in data:
        out["content"] = data["content"]
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    return out
