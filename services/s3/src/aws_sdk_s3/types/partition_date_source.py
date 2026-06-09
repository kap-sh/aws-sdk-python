"""Generated from Smithy shape ``com.amazonaws.s3#PartitionDateSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

PartitionDateSource: TypeAlias = Literal[
    "EventTime",
    "DeliveryTime",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EventTime",
        "DeliveryTime",
    )
)


def to_xml_text(value: PartitionDateSource) -> str:
    return value


def from_xml_text(text: str) -> PartitionDateSource:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PartitionDateSource value: {text!r}")
    return cast(PartitionDateSource, text)


def serialize_xml(value: PartitionDateSource, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> PartitionDateSource:
    return from_xml_text(el.text or "")
