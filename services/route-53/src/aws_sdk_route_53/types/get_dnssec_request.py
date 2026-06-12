"""Generated from Smithy shape ``com.amazonaws.route53#GetDNSSECRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_id


class GetDNSSECRequest(TypedDict):
    hosted_zone_id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>A unique string used to identify a hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetDNSSECRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetDNSSECRequest:
    out: GetDNSSECRequest = {}  # type: ignore[typeddict-item]
    return out
