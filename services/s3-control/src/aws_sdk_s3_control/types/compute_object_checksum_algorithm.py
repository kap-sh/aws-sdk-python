"""Generated from Smithy shape ``com.amazonaws.s3control#ComputeObjectChecksumAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

ComputeObjectChecksumAlgorithm: TypeAlias = Literal[
    "CRC32",
    "CRC32C",
    "CRC64NVME",
    "MD5",
    "SHA1",
    "SHA256",
    "SHA512",
    "XXHASH64",
    "XXHASH3",
    "XXHASH128",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRC32",
        "CRC32C",
        "CRC64NVME",
        "MD5",
        "SHA1",
        "SHA256",
        "SHA512",
        "XXHASH64",
        "XXHASH3",
        "XXHASH128",
    )
)


def to_xml_text(value: ComputeObjectChecksumAlgorithm) -> str:
    return value


def from_xml_text(text: str) -> ComputeObjectChecksumAlgorithm:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ComputeObjectChecksumAlgorithm value: {text!r}"
        )
    return cast(ComputeObjectChecksumAlgorithm, text)


def serialize_xml(
    value: ComputeObjectChecksumAlgorithm, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ComputeObjectChecksumAlgorithm:
    return from_xml_text(el.text or "")
