"""Generated from Smithy shape ``com.amazonaws.route53#GetHostedZoneLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.hosted_zone_limit_type
    import capo_route_53.types.resource_id


class GetHostedZoneLimitRequest(TypedDict, closed=True):
    type: "capo_route_53.types.hosted_zone_limit_type.HostedZoneLimitType"
    """<p>The limit that you want to get. Valid values include the following:</p> <ul> <li> <p> <b>MAX_RRSETS_BY_ZONE</b>: The maximum number of records that you can create in the specified hosted zone.</p> </li> <li> <p> <b>MAX_VPCS_ASSOCIATED_BY_ZONE</b>: The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.</p> </li> </ul>"""
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that you want to get a limit for.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetHostedZoneLimitRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetHostedZoneLimitRequest:
    out: GetHostedZoneLimitRequest = {}  # type: ignore[typeddict-item]
    return out
