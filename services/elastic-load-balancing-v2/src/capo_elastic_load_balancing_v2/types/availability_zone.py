"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AvailabilityZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.load_balancer_addresses
    import capo_elastic_load_balancing_v2.types.outpost_id
    import capo_elastic_load_balancing_v2.types.source_nat_ipv6_prefixes
    import capo_elastic_load_balancing_v2.types.subnet_id
    import capo_elastic_load_balancing_v2.types.zone_name


class AvailabilityZone(TypedDict, closed=True):
    zone_name: NotRequired["capo_elastic_load_balancing_v2.types.zone_name.ZoneName"]
    """<p>The name of the Availability Zone.</p>"""
    subnet_id: NotRequired["capo_elastic_load_balancing_v2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet. You can specify one subnet per Availability Zone.</p>"""
    outpost_id: NotRequired["capo_elastic_load_balancing_v2.types.outpost_id.OutpostId"]
    """<p>[Application Load Balancers on Outposts] The ID of the Outpost.</p>"""
    load_balancer_addresses: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_addresses.LoadBalancerAddresses"
    ]
    """<p>[Network Load Balancers] If you need static IP addresses for your load balancer, you can specify one Elastic IP address per Availability Zone when you create an internal-facing load balancer. For internal load balancers, you can specify a private IP address from the IPv4 range of the subnet.</p>"""
    source_nat_ipv6_prefixes: NotRequired[
        "capo_elastic_load_balancing_v2.types.source_nat_ipv6_prefixes.SourceNatIpv6Prefixes"
    ]
    """<p>[Network Load Balancers with UDP listeners] The IPv6 prefixes to use for source NAT. For each subnet, specify an IPv6 prefix (/80 netmask) from the subnet CIDR block or <code>auto_assigned</code> to use an IPv6 prefix selected at random from the subnet CIDR block.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZone, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "zone_name" in value:
        pairs.append((f"{prefix}.ZoneName", str(value["zone_name"])))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "outpost_id" in value:
        pairs.append((f"{prefix}.OutpostId", str(value["outpost_id"])))
    if "load_balancer_addresses" in value:
        import capo_elastic_load_balancing_v2.types.load_balancer_addresses

        capo_elastic_load_balancing_v2.types.load_balancer_addresses.serialize_query(
            value["load_balancer_addresses"], pairs, f"{prefix}.LoadBalancerAddresses"
        )
    if "source_nat_ipv6_prefixes" in value:
        import capo_elastic_load_balancing_v2.types.source_nat_ipv6_prefixes

        capo_elastic_load_balancing_v2.types.source_nat_ipv6_prefixes.serialize_query(
            value["source_nat_ipv6_prefixes"], pairs, f"{prefix}.SourceNatIpv6Prefixes"
        )


def deserialize_query(el: Element) -> AvailabilityZone:
    out: AvailabilityZone = {}  # type: ignore[typeddict-item]
    child_zone_name = el.find("ZoneName")
    if child_zone_name is not None:
        out["zone_name"] = str(child_zone_name.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_outpost_id = el.find("OutpostId")
    if child_outpost_id is not None:
        out["outpost_id"] = str(child_outpost_id.text or "")
    child_load_balancer_addresses = el.find("LoadBalancerAddresses")
    if child_load_balancer_addresses is not None:
        import capo_elastic_load_balancing_v2.types.load_balancer_addresses

        out["load_balancer_addresses"] = (
            capo_elastic_load_balancing_v2.types.load_balancer_addresses.deserialize_query(
                child_load_balancer_addresses
            )
        )
    child_source_nat_ipv6_prefixes = el.find("SourceNatIpv6Prefixes")
    if child_source_nat_ipv6_prefixes is not None:
        import capo_elastic_load_balancing_v2.types.source_nat_ipv6_prefixes

        out["source_nat_ipv6_prefixes"] = (
            capo_elastic_load_balancing_v2.types.source_nat_ipv6_prefixes.deserialize_query(
                child_source_nat_ipv6_prefixes
            )
        )
    return out
