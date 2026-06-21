"""Generated from Smithy shape ``com.amazonaws.polly#CloseStreamEvent``."""

from typing import TypedDict

from aws_sdk_polly._protocol.eventstream import HeaderValue, Message


class CloseStreamEvent(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CloseStreamEvent) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CloseStreamEvent:
    out: CloseStreamEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: CloseStreamEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "CloseStreamEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> CloseStreamEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: CloseStreamEvent = {}  # type: ignore[typeddict-item]
    return out
