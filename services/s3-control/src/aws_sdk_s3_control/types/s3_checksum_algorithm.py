"""Generated from Smithy shape ``com.amazonaws.s3control#S3ChecksumAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

S3ChecksumAlgorithm: TypeAlias = Literal[
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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def to_xml_text(value: S3ChecksumAlgorithm) -> str:
    return value


def from_xml_text(text: str) -> S3ChecksumAlgorithm:
    if text not in _VALUES:
        raise DeserializationError(f"unknown S3ChecksumAlgorithm value: {text!r}")
    return cast(S3ChecksumAlgorithm, text)


def serialize_xml(value: S3ChecksumAlgorithm, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3ChecksumAlgorithm:
    return from_xml_text(el.text or "")
