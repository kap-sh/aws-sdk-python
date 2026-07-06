"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageContentBlockStopEvent``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent._protocol.eventstream import HeaderValue, Message


class SendMessageContentBlockStopEvent(TypedDict, closed=True):
    index: NotRequired["int"]
    """<p>Zero-based index of the content block</p>"""
    type: NotRequired["str"]
    """<p>The type of content in this block</p>"""
    text: NotRequired["str"]
    """<p>The accumulated complete content text</p>"""
    last: NotRequired["bool"]
    """<p>Whether this is the final content block in the response</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageContentBlockStopEvent) -> dict:
    out: dict = {}
    if "index" in value:
        out["index"] = value["index"]
    if "type" in value:
        out["type"] = value["type"]
    if "text" in value:
        out["text"] = value["text"]
    if "last" in value:
        out["last"] = value["last"]
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageContentBlockStopEvent:
    out: SendMessageContentBlockStopEvent = {}  # type: ignore[typeddict-item]
    if "index" in data:
        out["index"] = data["index"]
    if "type" in data:
        out["type"] = data["type"]
    if "text" in data:
        out["text"] = data["text"]
    if "last" in data:
        out["last"] = data["last"]
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    return out


def serialize_event_json(value: SendMessageContentBlockStopEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "contentBlockStop"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> SendMessageContentBlockStopEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SendMessageContentBlockStopEvent = {}  # type: ignore[typeddict-item]
    return out
