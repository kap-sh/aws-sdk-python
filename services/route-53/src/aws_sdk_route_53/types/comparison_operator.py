"""Generated from Smithy shape ``com.amazonaws.route53#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanThreshold",
    "LessThanOrEqualToThreshold",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GreaterThanOrEqualToThreshold",
        "GreaterThanThreshold",
        "LessThanThreshold",
        "LessThanOrEqualToThreshold",
    )
)


def to_xml_text(value: ComparisonOperator) -> str:
    return value


def from_xml_text(text: str) -> ComparisonOperator:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {text!r}")
    return cast(ComparisonOperator, text)


def serialize_xml(value: ComparisonOperator, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ComparisonOperator:
    return from_xml_text(el.text or "")
