"""Generated from Smithy shape ``com.amazonaws.route53#TestDNSAnswerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.dns_name
    import aws_sdk_route_53.types.ip_address
    import aws_sdk_route_53.types.resource_id
    import aws_sdk_route_53.types.rr_type
    import aws_sdk_route_53.types.subnet_mask


class TestDNSAnswerRequest(TypedDict, closed=True):
    hosted_zone_id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that you want Amazon Route 53 to simulate a query for.</p>"""
    record_name: "aws_sdk_route_53.types.dns_name.DNSName"
    """<p>The name of the resource record set that you want Amazon Route 53 to simulate a query for.</p>"""
    record_type: "aws_sdk_route_53.types.rr_type.RRType"
    """<p>The type of the resource record set.</p>"""
    resolver_ip: NotRequired["aws_sdk_route_53.types.ip_address.IPAddress"]
    """<p>If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, <code>TestDnsAnswer</code> uses the IP address of a DNS resolver in the Amazon Web Services US East (N. Virginia) Region (<code>us-east-1</code>).</p>"""
    edns0_client_subnet_ip: NotRequired["aws_sdk_route_53.types.ip_address.IPAddress"]
    """<p>If the resolver that you specified for resolverip supports EDNS0, specify the IPv4 or IPv6 address of a client in the applicable location, for example, <code>192.0.2.44</code> or <code>2001:db8:85a3::8a2e:370:7334</code>.</p>"""
    edns0_client_subnet_mask: NotRequired[
        "aws_sdk_route_53.types.subnet_mask.SubnetMask"
    ]
    """<p>If you specify an IP address for <code>edns0clientsubnetip</code>, you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify <code>192.0.2.44</code> for <code>edns0clientsubnetip</code> and <code>24</code> for <code>edns0clientsubnetmask</code>, the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits for IPv4 addresses and 64 bits for IPv6 addresses.</p> <p>The range of valid values depends on whether <code>edns0clientsubnetip</code> is an IPv4 or an IPv6 address:</p> <ul> <li> <p> <b>IPv4</b>: Specify a value between 0 and 32</p> </li> <li> <p> <b>IPv6</b>: Specify a value between 0 and 128</p> </li> </ul>"""


# --- restXml ser/de ---
def serialize_xml(value: TestDNSAnswerRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> TestDNSAnswerRequest:
    out: TestDNSAnswerRequest = {}  # type: ignore[typeddict-item]
    return out
