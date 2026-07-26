"""Generated from Smithy shape ``com.amazonaws.s3control#S3SSEAlgorithm``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

S3SSEAlgorithm: TypeAlias = Literal[
    "AES256",
    "KMS",
]


# --- restXml ser/de ---
def to_xml_text(value: S3SSEAlgorithm) -> str:
    return value


def from_xml_text(text: str) -> S3SSEAlgorithm:
    return cast(S3SSEAlgorithm, text)


def serialize_xml(value: S3SSEAlgorithm, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3SSEAlgorithm:
    return from_xml_text(el.text or "")
