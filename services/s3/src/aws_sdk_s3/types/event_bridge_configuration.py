"""Generated from Smithy shape ``com.amazonaws.s3#EventBridgeConfiguration``."""

from typing import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement


class EventBridgeConfiguration(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: EventBridgeConfiguration, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> EventBridgeConfiguration:
    out: EventBridgeConfiguration = {}  # type: ignore[typeddict-item]
    return out
