"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteMonitoringSubscriptionResult``."""

from typing import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement


class DeleteMonitoringSubscriptionResult(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteMonitoringSubscriptionResult, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteMonitoringSubscriptionResult:
    out: DeleteMonitoringSubscriptionResult = {}  # type: ignore[typeddict-item]
    return out
