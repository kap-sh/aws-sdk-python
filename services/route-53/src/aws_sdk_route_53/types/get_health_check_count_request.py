"""Generated from Smithy shape ``com.amazonaws.route53#GetHealthCheckCountRequest``."""

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement


class GetHealthCheckCountRequest(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: GetHealthCheckCountRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetHealthCheckCountRequest:
    out: GetHealthCheckCountRequest = {}  # type: ignore[typeddict-item]
    return out
