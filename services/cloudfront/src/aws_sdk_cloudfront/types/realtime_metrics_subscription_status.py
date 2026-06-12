"""Generated from Smithy shape ``com.amazonaws.cloudfront#RealtimeMetricsSubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

RealtimeMetricsSubscriptionStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restXml ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def to_xml_text(value: RealtimeMetricsSubscriptionStatus) -> str:
    return value


def from_xml_text(text: str) -> RealtimeMetricsSubscriptionStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown RealtimeMetricsSubscriptionStatus value: {text!r}"
        )
    return cast(RealtimeMetricsSubscriptionStatus, text)


def serialize_xml(
    value: RealtimeMetricsSubscriptionStatus, parent: Element, tag: str
) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> RealtimeMetricsSubscriptionStatus:
    return from_xml_text(el.text or "")
