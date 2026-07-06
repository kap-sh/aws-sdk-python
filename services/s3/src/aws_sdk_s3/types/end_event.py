"""Generated from Smithy shape ``com.amazonaws.s3#EndEvent``."""

from typing_extensions import TypedDict

from aws_sdk_s3._protocol.eventstream import HeaderValue, Message
from aws_sdk_s3._protocol.xml import Element, SubElement


class EndEvent(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: EndEvent, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> EndEvent:
    out: EndEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_xml(value: EndEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "End"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_xml(message: Message) -> EndEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: EndEvent = {}  # type: ignore[typeddict-item]
    return out
