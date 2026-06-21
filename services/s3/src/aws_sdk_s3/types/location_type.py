"""Generated from Smithy shape ``com.amazonaws.s3#LocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

LocationType: TypeAlias = Literal[
    "AvailabilityZone",
    "LocalZone",
]


# --- restXml ser/de ---
def to_xml_text(value: LocationType) -> str:
    return value


def from_xml_text(text: str) -> LocationType:
    return cast(LocationType, text)


def serialize_xml(value: LocationType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> LocationType:
    return from_xml_text(el.text or "")
