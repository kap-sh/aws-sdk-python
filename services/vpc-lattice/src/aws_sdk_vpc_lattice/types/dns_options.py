"""Generated from Smithy shape ``com.amazonaws.vpclattice#DnsOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.private_dns_preference
    import aws_sdk_vpc_lattice.types.private_dns_specified_domains_list


class DnsOptions(TypedDict, closed=True):
    private_dns_preference: NotRequired[
        "aws_sdk_vpc_lattice.types.private_dns_preference.PrivateDnsPreference"
    ]
    """<p> The preference for which private domains have a private hosted zone created for and associated with the specified VPC. Only supported when private DNS is enabled and when the VPC endpoint type is ServiceNetwork or Resource. </p> <ul> <li> <p> <code>ALL_DOMAINS</code> - VPC Lattice provisions private hosted zones for all custom domain names.</p> </li> <li> <p> <code>VERIFIED_DOMAINS_ONLY</code> - VPC Lattice provisions a private hosted zone only if custom domain name has been verified by the provider.</p> </li> <li> <p> <code>VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS</code> - VPC Lattice provisions private hosted zones for all verified custom domain names and other domain names that the resource consumer specifies. The resource consumer specifies the domain names in the privateDnsSpecifiedDomains parameter.</p> </li> <li> <p> <code>SPECIFIED_DOMAINS_ONLY</code> - VPC Lattice provisions a private hosted zone for domain names specified by the resource consumer. The resource consumer specifies the domain names in the privateDnsSpecifiedDomains parameter.</p> </li> </ul>"""
    private_dns_specified_domains: NotRequired[
        "aws_sdk_vpc_lattice.types.private_dns_specified_domains_list.PrivateDnsSpecifiedDomainsList"
    ]
    """<p> Indicates which of the private domains to create private hosted zones for and associate with the specified VPC. Only supported when private DNS is enabled and the private DNS preference is <code>VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS</code> or <code>SPECIFIED_DOMAINS_ONLY</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DnsOptions) -> dict:
    out: dict = {}
    if "private_dns_preference" in value:
        out["privateDnsPreference"] = value["private_dns_preference"]
    if "private_dns_specified_domains" in value:
        import aws_sdk_vpc_lattice.types.private_dns_specified_domains_list

        out["privateDnsSpecifiedDomains"] = (
            aws_sdk_vpc_lattice.types.private_dns_specified_domains_list.serialize_json(
                value["private_dns_specified_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> DnsOptions:
    out: DnsOptions = {}  # type: ignore[typeddict-item]
    if "privateDnsPreference" in data:
        out["private_dns_preference"] = data["privateDnsPreference"]
    if "privateDnsSpecifiedDomains" in data:
        import aws_sdk_vpc_lattice.types.private_dns_specified_domains_list

        out["private_dns_specified_domains"] = (
            aws_sdk_vpc_lattice.types.private_dns_specified_domains_list.deserialize_json(
                data["privateDnsSpecifiedDomains"]
            )
        )
    return out
