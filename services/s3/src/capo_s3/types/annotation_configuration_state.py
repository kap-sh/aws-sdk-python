"""Generated from Smithy shape ``com.amazonaws.s3#AnnotationConfigurationState``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

AnnotationConfigurationState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restXml ser/de ---
def to_xml_text(value: AnnotationConfigurationState) -> str:
    return value


def from_xml_text(text: str) -> AnnotationConfigurationState:
    return cast(AnnotationConfigurationState, text)


def serialize_xml(
    value: AnnotationConfigurationState, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> AnnotationConfigurationState:
    return from_xml_text(el.text or "")
