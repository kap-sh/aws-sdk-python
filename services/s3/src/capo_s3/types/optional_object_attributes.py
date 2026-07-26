"""Generated from Smithy shape ``com.amazonaws.s3#OptionalObjectAttributes``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

OptionalObjectAttributes: TypeAlias = Literal["RestoreStatus",]


# --- restXml ser/de ---
def to_xml_text(value: OptionalObjectAttributes) -> str:
    return value


def from_xml_text(text: str) -> OptionalObjectAttributes:
    return cast(OptionalObjectAttributes, text)


def serialize_xml(value: OptionalObjectAttributes, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> OptionalObjectAttributes:
    return from_xml_text(el.text or "")
