"""Generated from Smithy shape ``com.amazonaws.cloudfront#ViewerMtlsMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

ViewerMtlsMode: TypeAlias = Literal[
    "required",
    "optional",
    "passthrough",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "required",
        "optional",
        "passthrough",
    )
)


def to_xml_text(value: ViewerMtlsMode) -> str:
    return value


def from_xml_text(text: str) -> ViewerMtlsMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ViewerMtlsMode value: {text!r}")
    return cast(ViewerMtlsMode, text)


def serialize_xml(value: ViewerMtlsMode, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ViewerMtlsMode:
    return from_xml_text(el.text or "")
