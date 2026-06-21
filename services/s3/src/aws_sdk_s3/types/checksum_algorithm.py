"""Generated from Smithy shape ``com.amazonaws.s3#ChecksumAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3._protocol.xml import Element, SubElement

ChecksumAlgorithm: TypeAlias = Literal[
    "CRC32",
    "CRC32C",
    "SHA1",
    "SHA256",
    "CRC64NVME",
    "SHA512",
    "MD5",
    "XXHASH64",
    "XXHASH3",
    "XXHASH128",
]


# --- restXml ser/de ---
def to_xml_text(value: ChecksumAlgorithm) -> str:
    return value


def from_xml_text(text: str) -> ChecksumAlgorithm:
    return cast(ChecksumAlgorithm, text)


def serialize_xml(value: ChecksumAlgorithm, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ChecksumAlgorithm:
    return from_xml_text(el.text or "")
