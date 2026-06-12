"""Generated from Smithy shape ``com.amazonaws.route53#DeleteHealthCheckResponse``."""

from typing import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement


class DeleteHealthCheckResponse(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: DeleteHealthCheckResponse, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteHealthCheckResponse:
    out: DeleteHealthCheckResponse = {}  # type: ignore[typeddict-item]
    return out
