"""Generated from Smithy shape ``com.amazonaws.s3control#AsyncOperationName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

AsyncOperationName: TypeAlias = Literal[
    "CreateMultiRegionAccessPoint",
    "DeleteMultiRegionAccessPoint",
    "PutMultiRegionAccessPointPolicy",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreateMultiRegionAccessPoint",
        "DeleteMultiRegionAccessPoint",
        "PutMultiRegionAccessPointPolicy",
    )
)


def to_xml_text(value: AsyncOperationName) -> str:
    return value


def from_xml_text(text: str) -> AsyncOperationName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AsyncOperationName value: {text!r}")
    return cast(AsyncOperationName, text)


def serialize_xml(value: AsyncOperationName, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> AsyncOperationName:
    return from_xml_text(el.text or "")
