"""Generated from Smithy shape ``com.amazonaws.s3#TableSseAlgorithm``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

TableSseAlgorithm: TypeAlias = Literal[
    "aws:kms",
    "AES256",
]


# --- restXml ser/de ---
def to_xml_text(value: TableSseAlgorithm) -> str:
    return value


def from_xml_text(text: str) -> TableSseAlgorithm:
    return cast(TableSseAlgorithm, text)


def serialize_xml(value: TableSseAlgorithm, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> TableSseAlgorithm:
    return from_xml_text(el.text or "")
