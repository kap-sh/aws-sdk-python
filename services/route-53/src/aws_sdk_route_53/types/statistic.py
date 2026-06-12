"""Generated from Smithy shape ``com.amazonaws.route53#Statistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

Statistic: TypeAlias = Literal[
    "Average",
    "Sum",
    "SampleCount",
    "Maximum",
    "Minimum",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Average",
        "Sum",
        "SampleCount",
        "Maximum",
        "Minimum",
    )
)


def to_xml_text(value: Statistic) -> str:
    return value


def from_xml_text(text: str) -> Statistic:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Statistic value: {text!r}")
    return cast(Statistic, text)


def serialize_xml(value: Statistic, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> Statistic:
    return from_xml_text(el.text or "")
