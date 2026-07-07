"""Generated from Smithy shape ``com.amazonaws.route53#ListHostedZonesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.hosted_zone_type
    import aws_sdk_route_53.types.page_marker
    import aws_sdk_route_53.types.resource_id


class ListHostedZonesRequest(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_route_53.types.page_marker.PageMarker"]
    """<p>If the value of <code>IsTruncated</code> in the previous response was <code>true</code>, you have more hosted zones. To get more hosted zones, submit another <code>ListHostedZones</code> request. </p> <p>For the value of <code>marker</code>, specify the value of <code>NextMarker</code> from the previous response, which is the ID of the first hosted zone that Amazon Route 53 will return if you submit another request.</p> <p>If the value of <code>IsTruncated</code> in the previous response was <code>false</code>, there are no more hosted zones to get.</p>"""
    max_items: NotRequired["int"]
    """<p>(Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If you have more than <code>maxitems</code> hosted zones, the value of <code>IsTruncated</code> in the response is <code>true</code>, and the value of <code>NextMarker</code> is the hosted zone ID of the first hosted zone that Route 53 will return if you submit another request.</p>"""
    delegation_set_id: NotRequired["aws_sdk_route_53.types.resource_id.ResourceId"]
    """<p>If you're using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set. </p>"""
    hosted_zone_type: NotRequired[
        "aws_sdk_route_53.types.hosted_zone_type.HostedZoneType"
    ]
    """<p> (Optional) Specifies if the hosted zone is private. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListHostedZonesRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListHostedZonesRequest:
    out: ListHostedZonesRequest = {}  # type: ignore[typeddict-item]
    return out
