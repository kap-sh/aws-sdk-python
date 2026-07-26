"""Generated from Smithy shape ``com.amazonaws.s3#Payer``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

Payer: TypeAlias = Literal[
    "Requester",
    "BucketOwner",
]


# --- restXml ser/de ---
def to_xml_text(value: Payer) -> str:
    return value


def from_xml_text(text: str) -> Payer:
    return cast(Payer, text)


def serialize_xml(value: Payer, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Payer:
    return from_xml_text(el.text or "")
