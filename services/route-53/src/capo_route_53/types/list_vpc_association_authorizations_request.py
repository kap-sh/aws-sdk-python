"""Generated from Smithy shape ``com.amazonaws.route53#ListVPCAssociationAuthorizationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.pagination_token
    import capo_route_53.types.resource_id


class ListVPCAssociationAuthorizationsRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone for which you want a list of VPCs that can be associated with the hosted zone.</p>"""
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p> <i>Optional</i>: If a response includes a <code>NextToken</code> element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of results, submit another request, and include the value of <code>NextToken</code> from the response in the <code>nexttoken</code> parameter in another <code>ListVPCAssociationAuthorizations</code> request.</p>"""
    max_results: NotRequired["int"]
    """<p> <i>Optional</i>: An integer that specifies the maximum number of VPCs that you want Amazon Route 53 to return. If you don't specify a value for <code>MaxResults</code>, Route 53 returns up to 50 VPCs per page.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListVPCAssociationAuthorizationsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListVPCAssociationAuthorizationsRequest:
    out: ListVPCAssociationAuthorizationsRequest = {}  # type: ignore[typeddict-item]
    return out
