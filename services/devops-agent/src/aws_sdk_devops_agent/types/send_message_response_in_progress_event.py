"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageResponseInProgressEvent``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent._protocol.eventstream import HeaderValue, Message


class SendMessageResponseInProgressEvent(TypedDict, closed=True):
    response_id: NotRequired["str"]
    """<p>The response ID</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageResponseInProgressEvent) -> dict:
    out: dict = {}
    if "response_id" in value:
        out["responseId"] = value["response_id"]
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageResponseInProgressEvent:
    out: SendMessageResponseInProgressEvent = {}  # type: ignore[typeddict-item]
    if "responseId" in data:
        out["response_id"] = data["responseId"]
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    return out


def serialize_event_json(value: SendMessageResponseInProgressEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "responseInProgress"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> SendMessageResponseInProgressEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SendMessageResponseInProgressEvent = {}  # type: ignore[typeddict-item]
    return out
