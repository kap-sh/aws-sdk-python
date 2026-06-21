"""Generated from Smithy shape ``com.amazonaws.route53#CidrCollectionChangeAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement

CidrCollectionChangeAction: TypeAlias = Literal[
    "PUT",
    "DELETE_IF_EXISTS",
]


# --- restXml ser/de ---
def to_xml_text(value: CidrCollectionChangeAction) -> str:
    return value


def from_xml_text(text: str) -> CidrCollectionChangeAction:
    return cast(CidrCollectionChangeAction, text)


def serialize_xml(value: CidrCollectionChangeAction, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> CidrCollectionChangeAction:
    return from_xml_text(el.text or "")
