"""Generated from Smithy shape ``com.amazonaws.s3#ContinuationEvent``."""

from typing import TypedDict

from aws_sdk_s3._protocol.eventstream import HeaderValue, Message
from aws_sdk_s3._protocol.xml import Element, SubElement


class ContinuationEvent(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: ContinuationEvent, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ContinuationEvent:
    out: ContinuationEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_xml(value: ContinuationEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "Cont"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_xml(message: Message) -> ContinuationEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ContinuationEvent = {}  # type: ignore[typeddict-item]
    return out
