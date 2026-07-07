"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageResponseFailedEvent``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent._protocol.eventstream import HeaderValue, Message


class SendMessageResponseFailedEvent(TypedDict, closed=True):
    response_id: NotRequired["str"]
    """<p>The response ID</p>"""
    error_code: NotRequired["str"]
    """<p>Error code</p>"""
    error_message: NotRequired["str"]
    """<p>Error message</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageResponseFailedEvent) -> dict:
    out: dict = {}
    if "response_id" in value:
        out["responseId"] = value["response_id"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageResponseFailedEvent:
    out: SendMessageResponseFailedEvent = {}  # type: ignore[typeddict-item]
    if "responseId" in data:
        out["response_id"] = data["responseId"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "sequenceNumber" in data:
        out["sequence_number"] = data["sequenceNumber"]
    return out


def serialize_event_json(value: SendMessageResponseFailedEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "responseFailed"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> SendMessageResponseFailedEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SendMessageResponseFailedEvent = {}  # type: ignore[typeddict-item]
    return out
