"""Generated from Smithy shape ``com.amazonaws.s3#AnnotationDirective``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

AnnotationDirective: TypeAlias = Literal[
    "COPY",
    "EXCLUDE",
]


# --- restXml ser/de ---
def to_xml_text(value: AnnotationDirective) -> str:
    return value


def from_xml_text(text: str) -> AnnotationDirective:
    return cast(AnnotationDirective, text)


def serialize_xml(value: AnnotationDirective, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> AnnotationDirective:
    return from_xml_text(el.text or "")
