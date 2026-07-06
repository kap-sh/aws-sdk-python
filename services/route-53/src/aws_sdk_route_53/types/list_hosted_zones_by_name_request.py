"""Generated from Smithy shape ``com.amazonaws.route53#ListHostedZonesByNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.dns_name
    import aws_sdk_route_53.types.resource_id


class ListHostedZonesByNameRequest(TypedDict, closed=True):
    dns_name: NotRequired["aws_sdk_route_53.types.dns_name.DNSName"]
    """<p>(Optional) For your first request to <code>ListHostedZonesByName</code>, include the <code>dnsname</code> parameter only if you want to specify the name of the first hosted zone in the response. If you don't include the <code>dnsname</code> parameter, Amazon Route 53 returns all of the hosted zones that were created by the current Amazon Web Services account, in ASCII order. For subsequent requests, include both <code>dnsname</code> and <code>hostedzoneid</code> parameters. For <code>dnsname</code>, specify the value of <code>NextDNSName</code> from the previous response.</p>"""
    hosted_zone_id: NotRequired["aws_sdk_route_53.types.resource_id.ResourceId"]
    """<p>(Optional) For your first request to <code>ListHostedZonesByName</code>, do not include the <code>hostedzoneid</code> parameter.</p> <p>If you have more hosted zones than the value of <code>maxitems</code>, <code>ListHostedZonesByName</code> returns only the first <code>maxitems</code> hosted zones. To get the next group of <code>maxitems</code> hosted zones, submit another request to <code>ListHostedZonesByName</code> and include both <code>dnsname</code> and <code>hostedzoneid</code> parameters. For the value of <code>hostedzoneid</code>, specify the value of the <code>NextHostedZoneId</code> element from the previous response.</p>"""
    max_items: NotRequired["int"]
    """<p>The maximum number of hosted zones to be included in the response body for this request. If you have more than <code>maxitems</code> hosted zones, then the value of the <code>IsTruncated</code> element in the response is true, and the values of <code>NextDNSName</code> and <code>NextHostedZoneId</code> specify the first hosted zone in the next group of <code>maxitems</code> hosted zones. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListHostedZonesByNameRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListHostedZonesByNameRequest:
    out: ListHostedZonesByNameRequest = {}  # type: ignore[typeddict-item]
    return out
