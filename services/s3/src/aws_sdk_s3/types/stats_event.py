"""Generated from Smithy shape ``com.amazonaws.s3#StatsEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.eventstream import HeaderValue, Message
from aws_sdk_s3._protocol.xml import Element, SubElement, fromstring, tostring

if TYPE_CHECKING:
    import aws_sdk_s3.types.stats


class StatsEvent(TypedDict, closed=True):
    details: NotRequired["aws_sdk_s3.types.stats.Stats"]
    """<p>The Stats event details.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StatsEvent, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> StatsEvent:
    out: StatsEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_xml(value: StatsEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "Stats"}
    payload = b""
    import aws_sdk_s3.types.stats

    _payload_root = Element("_")
    aws_sdk_s3.types.stats.serialize_xml(value["details"], _payload_root, "Details")
    payload = tostring(_payload_root[0])
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_xml(message: Message) -> StatsEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: StatsEvent = {}  # type: ignore[typeddict-item]
    if payload:
        import aws_sdk_s3.types.stats

        out["details"] = aws_sdk_s3.types.stats.deserialize_xml(fromstring(payload))
    return out
