"""Generated from Smithy shape ``com.amazonaws.s3#TransitionDefaultMinimumObjectSize``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

TransitionDefaultMinimumObjectSize: TypeAlias = Literal[
    "varies_by_storage_class",
    "all_storage_classes_128K",
]


# --- restXml ser/de ---
def to_xml_text(value: TransitionDefaultMinimumObjectSize) -> str:
    return value


def from_xml_text(text: str) -> TransitionDefaultMinimumObjectSize:
    return cast(TransitionDefaultMinimumObjectSize, text)


def serialize_xml(
    value: TransitionDefaultMinimumObjectSize, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> TransitionDefaultMinimumObjectSize:
    return from_xml_text(el.text or "")
