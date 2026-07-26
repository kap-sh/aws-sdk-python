"""Generated from Smithy shape ``com.amazonaws.s3control#GranteeType``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

GranteeType: TypeAlias = Literal[
    "DIRECTORY_USER",
    "DIRECTORY_GROUP",
    "IAM",
]


# --- restXml ser/de ---
def to_xml_text(value: GranteeType) -> str:
    return value


def from_xml_text(text: str) -> GranteeType:
    return cast(GranteeType, text)


def serialize_xml(value: GranteeType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> GranteeType:
    return from_xml_text(el.text or "")
