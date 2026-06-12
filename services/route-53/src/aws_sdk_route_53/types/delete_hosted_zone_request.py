"""Generated from Smithy shape ``com.amazonaws.route53#DeleteHostedZoneRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_id


class DeleteHostedZoneRequest(TypedDict):
    id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone you want to delete.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteHostedZoneRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteHostedZoneRequest:
    out: DeleteHostedZoneRequest = {}  # type: ignore[typeddict-item]
    return out
