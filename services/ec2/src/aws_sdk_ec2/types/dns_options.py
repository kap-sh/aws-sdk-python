"""Generated from Smithy shape ``com.amazonaws.ec2#DnsOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.dns_record_ip_type
    import aws_sdk_ec2.types.private_dns_specified_domain_set
    import aws_sdk_ec2.types.string


class DnsOptions(TypedDict):
    dns_record_ip_type: NotRequired[
        "aws_sdk_ec2.types.dns_record_ip_type.DnsRecordIpType"
    ]
    """<p>The DNS records created for the endpoint.</p>"""
    private_dns_only_for_inbound_resolver_endpoint: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether to enable private DNS only for inbound endpoints.</p>"""
    private_dns_preference: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The preference for which private domains have a private hosted zone created for and associated with the specified VPC. Only supported when private DNS is enabled and when the VPC endpoint type is ServiceNetwork or Resource. </p> <ul> <li> <p> <code>ALL_DOMAINS</code> - VPC Lattice provisions private hosted zones for all custom domain names.</p> </li> <li> <p> <code>VERIFIED_DOMAINS_ONLY</code> - VPC Lattice provisions a private hosted zone only if custom domain name has been verified by the provider.</p> </li> <li> <p> <code>VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS</code> - VPC Lattice provisions private hosted zones for all verified custom domain names and other domain names that the resource consumer specifies. The resource consumer specifies the domain names in the PrivateDnsSpecifiedDomains parameter.</p> </li> <li> <p> <code>SPECIFIED_DOMAINS_ONLY</code> - VPC Lattice provisions a private hosted zone for domain names specified by the resource consumer. The resource consumer specifies the domain names in the PrivateDnsSpecifiedDomains parameter.</p> </li> </ul>"""
    private_dns_specified_domains: NotRequired[
        "aws_sdk_ec2.types.private_dns_specified_domain_set.PrivateDnsSpecifiedDomainSet"
    ]
    """<p> Indicates which of the private domains to create private hosted zones for and associate with the specified VPC. Only supported when private DNS is enabled and the private DNS preference is <code>VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS</code> or <code>SPECIFIED_DOMAINS_ONLY</code>. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DnsOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dns_record_ip_type" in value:
        import aws_sdk_ec2.types.dns_record_ip_type

        aws_sdk_ec2.types.dns_record_ip_type.serialize_ec2_query(
            value["dns_record_ip_type"], pairs, f"{prefix}.DnsRecordIpType"
        )
    if "private_dns_only_for_inbound_resolver_endpoint" in value:
        pairs.append(
            (
                f"{prefix}.PrivateDnsOnlyForInboundResolverEndpoint",
                "true"
                if value["private_dns_only_for_inbound_resolver_endpoint"]
                else "false",
            )
        )
    if "private_dns_preference" in value:
        pairs.append(
            (f"{prefix}.PrivateDnsPreference", str(value["private_dns_preference"]))
        )
    if "private_dns_specified_domains" in value:
        import aws_sdk_ec2.types.private_dns_specified_domain_set

        aws_sdk_ec2.types.private_dns_specified_domain_set.serialize_ec2_query(
            value["private_dns_specified_domains"],
            pairs,
            f"{prefix}.PrivateDnsSpecifiedDomainSet",
        )


def deserialize_ec2_query(el: Element) -> DnsOptions:
    out: DnsOptions = {}  # type: ignore[typeddict-item]
    child_dns_record_ip_type = el.find("DnsRecordIpType")
    if child_dns_record_ip_type is not None:
        import aws_sdk_ec2.types.dns_record_ip_type

        out["dns_record_ip_type"] = (
            aws_sdk_ec2.types.dns_record_ip_type.deserialize_ec2_query(
                child_dns_record_ip_type
            )
        )
    child_private_dns_only_for_inbound_resolver_endpoint = el.find(
        "PrivateDnsOnlyForInboundResolverEndpoint"
    )
    if child_private_dns_only_for_inbound_resolver_endpoint is not None:
        out["private_dns_only_for_inbound_resolver_endpoint"] = (
            child_private_dns_only_for_inbound_resolver_endpoint.text or ""
        ).lower() == "true"
    child_private_dns_preference = el.find("PrivateDnsPreference")
    if child_private_dns_preference is not None:
        out["private_dns_preference"] = str(child_private_dns_preference.text or "")
    if el.find("PrivateDnsSpecifiedDomainSet") is not None:
        import aws_sdk_ec2.types.private_dns_specified_domain_set

        out["private_dns_specified_domains"] = (
            aws_sdk_ec2.types.private_dns_specified_domain_set.deserialize_ec2_query(
                el, "PrivateDnsSpecifiedDomainSet"
            )
        )
    return out
