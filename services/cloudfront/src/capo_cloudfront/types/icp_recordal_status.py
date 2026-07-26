"""Generated from Smithy shape ``com.amazonaws.cloudfront#ICPRecordalStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudfront._protocol.xml import Element, SubElement

ICPRecordalStatus: TypeAlias = Literal[
    "APPROVED",
    "SUSPENDED",
    "PENDING",
]


# --- restXml ser/de ---
def to_xml_text(value: ICPRecordalStatus) -> str:
    return value


def from_xml_text(text: str) -> ICPRecordalStatus:
    return cast(ICPRecordalStatus, text)


def serialize_xml(value: ICPRecordalStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ICPRecordalStatus:
    return from_xml_text(el.text or "")
