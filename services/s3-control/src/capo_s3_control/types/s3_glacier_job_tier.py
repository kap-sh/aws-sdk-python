"""Generated from Smithy shape ``com.amazonaws.s3control#S3GlacierJobTier``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

S3GlacierJobTier: TypeAlias = Literal[
    "BULK",
    "STANDARD",
]


# --- restXml ser/de ---
def to_xml_text(value: S3GlacierJobTier) -> str:
    return value


def from_xml_text(text: str) -> S3GlacierJobTier:
    return cast(S3GlacierJobTier, text)


def serialize_xml(value: S3GlacierJobTier, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3GlacierJobTier:
    return from_xml_text(el.text or "")
