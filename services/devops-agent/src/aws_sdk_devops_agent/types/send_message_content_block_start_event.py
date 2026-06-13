"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageContentBlockStartEvent``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SendMessageContentBlockStartEvent(TypedDict):
    index: NotRequired["int"]
    """<p>Zero-based index of the content block</p>"""
    type: NotRequired["str"]
    """<p>The type of content in this block</p>"""
    id: NotRequired["str"]
    """<p>Block identifier</p>"""
    parent_id: NotRequired["str"]
    """<p>Optional parent block ID for nested content blocks (e.g. subagent tool calls)</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageContentBlockStartEvent) -> dict:
    out: dict = {}
    if "index" in value:
        out["index"] = value["index"]
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "parent_id" in value:
        out["parentId"] = value["parent_id"]
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageContentBlockStartEvent:
    out: SendMessageContentBlockStartEvent = {}  # type: ignore[typeddict-item]
    if "index" in data:
        out["index"] = data["index"]
    if "type" in data:
        out["type"] = data["type"]
    if "id" in data:
        out["id"] = data["id"]
    if "parentId" in data:
        out["parent_id"] = data["parentId"]
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    return out
