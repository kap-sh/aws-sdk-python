"""Generated from Smithy shape ``com.amazonaws.s3#DataRedundancy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

DataRedundancy: TypeAlias = Literal[
    "SingleAvailabilityZone",
    "SingleLocalZone",
]


# --- restXml ser/de ---
def to_xml_text(value: DataRedundancy) -> str:
    return value


def from_xml_text(text: str) -> DataRedundancy:
    return cast(DataRedundancy, text)


def serialize_xml(value: DataRedundancy, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> DataRedundancy:
    return from_xml_text(el.text or "")
