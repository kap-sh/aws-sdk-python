"""Generated from Smithy shape ``com.amazonaws.ec2#DnsOptionsSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.dns_record_ip_type
    import aws_sdk_ec2.types.private_dns_specified_domain_set
    import aws_sdk_ec2.types.string


class DnsOptionsSpecification(TypedDict):
    dns_record_ip_type: NotRequired[
        "aws_sdk_ec2.types.dns_record_ip_type.DnsRecordIpType"
    ]
    """<p>The DNS records created for the endpoint.</p>"""
    private_dns_only_for_inbound_resolver_endpoint: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether to enable private DNS only for inbound endpoints. This option is available only for services that support both gateway and interface endpoints. It routes traffic that originates from the VPC to the gateway endpoint and traffic that originates from on-premises to the interface endpoint.</p>"""
    private_dns_preference: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The preference for which private domains have a private hosted zone created for and associated with the specified VPC. Only supported when private DNS is enabled and when the VPC endpoint type is ServiceNetwork or Resource. </p> <ul> <li> <p> <code>ALL_DOMAINS</code> - VPC Lattice provisions private hosted zones for all custom domain names.</p> </li> <li> <p> <code>VERIFIED_DOMAINS_ONLY</code> - VPC Lattice provisions a private hosted zone only if custom domain name has been verified by the provider.</p> </li> <li> <p> <code>VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS</code> - VPC Lattice provisions private hosted zones for all verified custom domain names and other domain names that the resource consumer specifies. The resource consumer specifies the domain names in the PrivateDnsSpecifiedDomains parameter.</p> </li> <li> <p> <code>SPECIFIED_DOMAINS_ONLY</code> - VPC Lattice provisions a private hosted zone for domain names specified by the resource consumer. The resource consumer specifies the domain names in the PrivateDnsSpecifiedDomains parameter.</p> </li> </ul>"""
    private_dns_specified_domains: NotRequired[
        "aws_sdk_ec2.types.private_dns_specified_domain_set.PrivateDnsSpecifiedDomainSet"
    ]
    """<p> Indicates which of the private domains to create private hosted zones for and associate with the specified VPC. Only supported when private DNS is enabled and the private DNS preference is verified-domains-and-specified-domains or specified-domains-only. </p>"""
