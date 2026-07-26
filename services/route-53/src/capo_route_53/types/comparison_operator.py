"""Generated from Smithy shape ``com.amazonaws.route53#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from capo_route_53._protocol.xml import Element, SubElement

ComparisonOperator: TypeAlias = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanThreshold",
    "LessThanOrEqualToThreshold",
]


# --- restXml ser/de ---
def to_xml_text(value: ComparisonOperator) -> str:
    return value


def from_xml_text(text: str) -> ComparisonOperator:
    return cast(ComparisonOperator, text)


def serialize_xml(value: ComparisonOperator, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ComparisonOperator:
    return from_xml_text(el.text or "")
