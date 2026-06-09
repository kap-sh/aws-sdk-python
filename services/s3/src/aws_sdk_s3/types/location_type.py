"""Generated from Smithy shape ``com.amazonaws.s3#LocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

LocationType: TypeAlias = Literal[
    "AvailabilityZone",
    "LocalZone",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AvailabilityZone",
        "LocalZone",
    )
)


def to_xml_text(value: LocationType) -> str:
    return value


def from_xml_text(text: str) -> LocationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LocationType value: {text!r}")
    return cast(LocationType, text)


def serialize_xml(value: LocationType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> LocationType:
    return from_xml_text(el.text or "")
