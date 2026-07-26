"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetConnectionGroupByRoutingEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetConnectionGroupByRoutingEndpointRequest(TypedDict, closed=True):
    routing_endpoint: "capo_cloudfront.types.string.string"
    """<p>The routing endpoint for the target connection group, such as d111111abcdef8.cloudfront.net.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetConnectionGroupByRoutingEndpointRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetConnectionGroupByRoutingEndpointRequest:
    out: GetConnectionGroupByRoutingEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
