"""Generated from Smithy shape ``com.amazonaws.route53#Statistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement

Statistic: TypeAlias = Literal[
    "Average",
    "Sum",
    "SampleCount",
    "Maximum",
    "Minimum",
]


# --- restXml ser/de ---
def to_xml_text(value: Statistic) -> str:
    return value


def from_xml_text(text: str) -> Statistic:
    return cast(Statistic, text)


def serialize_xml(value: Statistic, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Statistic:
    return from_xml_text(el.text or "")
