"""Generated from Smithy shape ``com.amazonaws.s3control#MFADeleteStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

MFADeleteStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
def to_xml_text(value: MFADeleteStatus) -> str:
    return value


def from_xml_text(text: str) -> MFADeleteStatus:
    return cast(MFADeleteStatus, text)


def serialize_xml(value: MFADeleteStatus, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> MFADeleteStatus:
    return from_xml_text(el.text or "")
