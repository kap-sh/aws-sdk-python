"""Generated from Smithy shape ``com.amazonaws.route53#ListHostedZonesByVPCRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.pagination_token
    import capo_route_53.types.vpc_id
    import capo_route_53.types.vpc_region


class ListHostedZonesByVPCRequest(TypedDict, closed=True):
    vpc_id: "capo_route_53.types.vpc_id.VPCId"
    """<p>The ID of the Amazon VPC that you want to list hosted zones for.</p>"""
    vpc_region: "capo_route_53.types.vpc_region.VPCRegion"
    """<p>For the Amazon VPC that you specified for <code>VPCId</code>, the Amazon Web Services Region that you created the VPC in. </p>"""
    max_items: NotRequired["int"]
    """<p>(Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If the specified VPC is associated with more than <code>MaxItems</code> hosted zones, the response includes a <code>NextToken</code> element. <code>NextToken</code> contains an encrypted token that identifies the first hosted zone that Route 53 will return if you submit another request.</p>"""
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p>If the previous response included a <code>NextToken</code> element, the specified VPC is associated with more hosted zones. To get more hosted zones, submit another <code>ListHostedZonesByVPC</code> request. </p> <p>For the value of <code>NextToken</code>, specify the value of <code>NextToken</code> from the previous response.</p> <p>If the previous response didn't include a <code>NextToken</code> element, there are no more hosted zones to get.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListHostedZonesByVPCRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListHostedZonesByVPCRequest:
    out: ListHostedZonesByVPCRequest = {}  # type: ignore[typeddict-item]
    return out
