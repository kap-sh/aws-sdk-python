"""Generated from Smithy shape ``com.amazonaws.s3control#NetworkOrigin``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement

NetworkOrigin: TypeAlias = Literal[
    "Internet",
    "VPC",
]


# --- restXml ser/de ---
def to_xml_text(value: NetworkOrigin) -> str:
    return value


def from_xml_text(text: str) -> NetworkOrigin:
    return cast(NetworkOrigin, text)


def serialize_xml(value: NetworkOrigin, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> NetworkOrigin:
    return from_xml_text(el.text or "")
