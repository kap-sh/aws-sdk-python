"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#LoadBalancer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.availability_zones
    import aws_sdk_elastic_load_balancing_v2.types.canonical_hosted_zone_id
    import aws_sdk_elastic_load_balancing_v2.types.created_time
    import aws_sdk_elastic_load_balancing_v2.types.customer_owned_ipv4_pool
    import aws_sdk_elastic_load_balancing_v2.types.dns_name
    import aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum
    import aws_sdk_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic
    import aws_sdk_elastic_load_balancing_v2.types.ip_address_type
    import aws_sdk_elastic_load_balancing_v2.types.ipam_pools
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_name
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_scheme_enum
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_state
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_type_enum
    import aws_sdk_elastic_load_balancing_v2.types.security_groups
    import aws_sdk_elastic_load_balancing_v2.types.vpc_id


class LoadBalancer(TypedDict):
    load_balancer_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    dns_name: NotRequired["aws_sdk_elastic_load_balancing_v2.types.dns_name.DNSName"]
    """<p>The public DNS name of the load balancer.</p>"""
    canonical_hosted_zone_id: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.canonical_hosted_zone_id.CanonicalHostedZoneId"
    ]
    """<p>The ID of the Amazon Route 53 hosted zone associated with the load balancer.</p>"""
    created_time: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.created_time.CreatedTime"
    ]
    """<p>The date and time the load balancer was created.</p>"""
    load_balancer_name: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_name.LoadBalancerName"
    ]
    """<p>The name of the load balancer.</p>"""
    scheme: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_scheme_enum.LoadBalancerSchemeEnum"
    ]
    """<p>The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.</p> <p>The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.</p>"""
    vpc_id: NotRequired["aws_sdk_elastic_load_balancing_v2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC for the load balancer.</p>"""
    state: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_state.LoadBalancerState"
    ]
    """<p>The state of the load balancer.</p>"""
    type: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_type_enum.LoadBalancerTypeEnum"
    ]
    """<p>The type of load balancer.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.availability_zones.AvailabilityZones"
    ]
    """<p>The subnets for the load balancer.</p>"""
    security_groups: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.security_groups.SecurityGroups"
    ]
    """<p>The IDs of the security groups for the load balancer.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.ip_address_type.IpAddressType"
    ]
    """<p>The type of IP addresses used for public or private connections by the subnets attached to your load balancer.</p> <p>[Application Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses), <code>dualstack</code> (IPv4 and IPv6 addresses), and <code>dualstack-without-public-ipv4</code> (public IPv6 addresses and private IPv4 and IPv6 addresses).</p> <p>[Network Load Balancers and Gateway Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses) and <code>dualstack</code> (IPv4 and IPv6 addresses).</p>"""
    customer_owned_ipv4_pool: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.customer_owned_ipv4_pool.CustomerOwnedIpv4Pool"
    ]
    """<p>[Application Load Balancers on Outposts] The ID of the customer-owned address pool.</p>"""
    enforce_security_group_inbound_rules_on_private_link_traffic: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.enforce_security_group_inbound_rules_on_private_link_traffic.EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic"
    ]
    """<p>Indicates whether to evaluate inbound security group rules for traffic sent to a Network Load Balancer through Amazon Web Services PrivateLink.</p>"""
    enable_prefix_for_ipv6_source_nat: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.EnablePrefixForIpv6SourceNatEnum"
    ]
    """<p>[Network Load Balancers with UDP listeners] Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be <code>dualstack</code>. The default value is <code>off</code>.</p>"""
    ipam_pools: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.ipam_pools.IpamPools"
    ]
    """<p>[Application Load Balancers] The IPAM pool in use by the load balancer, if configured.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_arn" in value:
        pairs.append((f"{prefix}.LoadBalancerArn", str(value["load_balancer_arn"])))
    if "dns_name" in value:
        pairs.append((f"{prefix}.DNSName", str(value["dns_name"])))
    if "canonical_hosted_zone_id" in value:
        pairs.append(
            (f"{prefix}.CanonicalHostedZoneId", str(value["canonical_hosted_zone_id"]))
        )
    if "created_time" in value:
        import aws_sdk_elastic_load_balancing_v2.types.created_time

        aws_sdk_elastic_load_balancing_v2.types.created_time.serialize_query(
            value["created_time"], pairs, f"{prefix}.CreatedTime"
        )
    if "load_balancer_name" in value:
        pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    if "scheme" in value:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_scheme_enum

        aws_sdk_elastic_load_balancing_v2.types.load_balancer_scheme_enum.serialize_query(
            value["scheme"], pairs, f"{prefix}.Scheme"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "state" in value:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_state

        aws_sdk_elastic_load_balancing_v2.types.load_balancer_state.serialize_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "type" in value:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_type_enum

        aws_sdk_elastic_load_balancing_v2.types.load_balancer_type_enum.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "availability_zones" in value:
        import aws_sdk_elastic_load_balancing_v2.types.availability_zones

        aws_sdk_elastic_load_balancing_v2.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZones"
        )
    if "security_groups" in value:
        import aws_sdk_elastic_load_balancing_v2.types.security_groups

        aws_sdk_elastic_load_balancing_v2.types.security_groups.serialize_query(
            value["security_groups"], pairs, f"{prefix}.SecurityGroups"
        )
    if "ip_address_type" in value:
        import aws_sdk_elastic_load_balancing_v2.types.ip_address_type

        aws_sdk_elastic_load_balancing_v2.types.ip_address_type.serialize_query(
            value["ip_address_type"], pairs, f"{prefix}.IpAddressType"
        )
    if "customer_owned_ipv4_pool" in value:
        pairs.append(
            (f"{prefix}.CustomerOwnedIpv4Pool", str(value["customer_owned_ipv4_pool"]))
        )
    if "enforce_security_group_inbound_rules_on_private_link_traffic" in value:
        pairs.append(
            (
                f"{prefix}.EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic",
                str(
                    value[
                        "enforce_security_group_inbound_rules_on_private_link_traffic"
                    ]
                ),
            )
        )
    if "enable_prefix_for_ipv6_source_nat" in value:
        import aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum

        aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.serialize_query(
            value["enable_prefix_for_ipv6_source_nat"],
            pairs,
            f"{prefix}.EnablePrefixForIpv6SourceNat",
        )
    if "ipam_pools" in value:
        import aws_sdk_elastic_load_balancing_v2.types.ipam_pools

        aws_sdk_elastic_load_balancing_v2.types.ipam_pools.serialize_query(
            value["ipam_pools"], pairs, f"{prefix}.IpamPools"
        )


def deserialize_query(el: Element) -> LoadBalancer:
    out: LoadBalancer = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_dns_name = el.find("DNSName")
    if child_dns_name is not None:
        out["dns_name"] = str(child_dns_name.text or "")
    child_canonical_hosted_zone_id = el.find("CanonicalHostedZoneId")
    if child_canonical_hosted_zone_id is not None:
        out["canonical_hosted_zone_id"] = str(child_canonical_hosted_zone_id.text or "")
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import aws_sdk_elastic_load_balancing_v2.types.created_time

        out["created_time"] = (
            aws_sdk_elastic_load_balancing_v2.types.created_time.deserialize_query(
                child_created_time
            )
        )
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    child_scheme = el.find("Scheme")
    if child_scheme is not None:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_scheme_enum

        out["scheme"] = (
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_scheme_enum.deserialize_query(
                child_scheme
            )
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_state

        out["state"] = (
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_state.deserialize_query(
                child_state
            )
        )
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_elastic_load_balancing_v2.types.load_balancer_type_enum

        out["type"] = (
            aws_sdk_elastic_load_balancing_v2.types.load_balancer_type_enum.deserialize_query(
                child_type
            )
        )
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import aws_sdk_elastic_load_balancing_v2.types.availability_zones

        out["availability_zones"] = (
            aws_sdk_elastic_load_balancing_v2.types.availability_zones.deserialize_query(
                child_availability_zones
            )
        )
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import aws_sdk_elastic_load_balancing_v2.types.security_groups

        out["security_groups"] = (
            aws_sdk_elastic_load_balancing_v2.types.security_groups.deserialize_query(
                child_security_groups
            )
        )
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import aws_sdk_elastic_load_balancing_v2.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_elastic_load_balancing_v2.types.ip_address_type.deserialize_query(
                child_ip_address_type
            )
        )
    child_customer_owned_ipv4_pool = el.find("CustomerOwnedIpv4Pool")
    if child_customer_owned_ipv4_pool is not None:
        out["customer_owned_ipv4_pool"] = str(child_customer_owned_ipv4_pool.text or "")
    child_enforce_security_group_inbound_rules_on_private_link_traffic = el.find(
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic"
    )
    if child_enforce_security_group_inbound_rules_on_private_link_traffic is not None:
        out["enforce_security_group_inbound_rules_on_private_link_traffic"] = str(
            child_enforce_security_group_inbound_rules_on_private_link_traffic.text
            or ""
        )
    child_enable_prefix_for_ipv6_source_nat = el.find("EnablePrefixForIpv6SourceNat")
    if child_enable_prefix_for_ipv6_source_nat is not None:
        import aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum

        out["enable_prefix_for_ipv6_source_nat"] = (
            aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.deserialize_query(
                child_enable_prefix_for_ipv6_source_nat
            )
        )
    child_ipam_pools = el.find("IpamPools")
    if child_ipam_pools is not None:
        import aws_sdk_elastic_load_balancing_v2.types.ipam_pools

        out["ipam_pools"] = (
            aws_sdk_elastic_load_balancing_v2.types.ipam_pools.deserialize_query(
                child_ipam_pools
            )
        )
    return out
