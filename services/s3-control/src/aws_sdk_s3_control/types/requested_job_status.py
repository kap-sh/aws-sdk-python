"""Generated from Smithy shape ``com.amazonaws.s3control#RequestedJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

RequestedJobStatus: TypeAlias = Literal[
    "Cancelled",
    "Ready",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Cancelled",
        "Ready",
    )
)


def to_xml_text(value: RequestedJobStatus) -> str:
    return value


def from_xml_text(text: str) -> RequestedJobStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RequestedJobStatus value: {text!r}")
    return cast(RequestedJobStatus, text)


def serialize_xml(value: RequestedJobStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> RequestedJobStatus:
    return from_xml_text(el.text or "")
