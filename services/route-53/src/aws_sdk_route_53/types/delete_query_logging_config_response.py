"""Generated from Smithy shape ``com.amazonaws.route53#DeleteQueryLoggingConfigResponse``."""

from typing import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement


class DeleteQueryLoggingConfigResponse(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteQueryLoggingConfigResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteQueryLoggingConfigResponse:
    out: DeleteQueryLoggingConfigResponse = {}  # type: ignore[typeddict-item]
    return out
