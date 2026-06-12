"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SetSubnetsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum
    import aws_sdk_elastic_load_balancing_v2.types.ip_address_type
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn
    import aws_sdk_elastic_load_balancing_v2.types.subnet_mappings
    import aws_sdk_elastic_load_balancing_v2.types.subnets


class SetSubnetsInput(TypedDict):
    load_balancer_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    subnets: NotRequired["aws_sdk_elastic_load_balancing_v2.types.subnets.Subnets"]
    """<p>The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.</p> <p>[Application Load Balancers] You must specify subnets from at least two Availability Zones.</p> <p>[Application Load Balancers on Outposts] You must specify one Outpost subnet.</p> <p>[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.</p> <p>[Network Load Balancers] You can specify subnets from one or more Availability Zones.</p> <p>[Gateway Load Balancers] You can specify subnets from one or more Availability Zones. You must include all subnets that were enabled previously, with their existing configurations, plus any additional subnets.</p>"""
    subnet_mappings: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.subnet_mappings.SubnetMappings"
    ]
    """<p>The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.</p> <p>[Application Load Balancers] You must specify subnets from at least two Availability Zones. You can't specify Elastic IP addresses for your subnets.</p> <p>[Application Load Balancers on Outposts] You must specify one Outpost subnet.</p> <p>[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.</p> <p>[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.</p> <p>[Gateway Load Balancers] You can specify subnets from one or more Availability Zones.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type.</p> <p>[Application Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses), <code>dualstack</code> (IPv4 and IPv6 addresses), and <code>dualstack-without-public-ipv4</code> (public IPv6 addresses and private IPv4 and IPv6 addresses).</p> <p>[Network Load Balancers and Gateway Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses) and <code>dualstack</code> (IPv4 and IPv6 addresses).</p>"""
    enable_prefix_for_ipv6_source_nat: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.EnablePrefixForIpv6SourceNatEnum"
    ]
    """<p>[Network Load Balancers with UDP listeners] Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be <code>dualstack</code>. The default value is <code>off</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetSubnetsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_arn" in value:
        pairs.append((f"{prefix}.LoadBalancerArn", str(value["load_balancer_arn"])))
    if "subnets" in value:
        import aws_sdk_elastic_load_balancing_v2.types.subnets

        aws_sdk_elastic_load_balancing_v2.types.subnets.serialize_query(
            value["subnets"], pairs, f"{prefix}.Subnets"
        )
    if "subnet_mappings" in value:
        import aws_sdk_elastic_load_balancing_v2.types.subnet_mappings

        aws_sdk_elastic_load_balancing_v2.types.subnet_mappings.serialize_query(
            value["subnet_mappings"], pairs, f"{prefix}.SubnetMappings"
        )
    if "ip_address_type" in value:
        import aws_sdk_elastic_load_balancing_v2.types.ip_address_type

        aws_sdk_elastic_load_balancing_v2.types.ip_address_type.serialize_query(
            value["ip_address_type"], pairs, f"{prefix}.IpAddressType"
        )
    if "enable_prefix_for_ipv6_source_nat" in value:
        import aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum

        aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.serialize_query(
            value["enable_prefix_for_ipv6_source_nat"],
            pairs,
            f"{prefix}.EnablePrefixForIpv6SourceNat",
        )


def deserialize_query(el: Element) -> SetSubnetsInput:
    out: SetSubnetsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import aws_sdk_elastic_load_balancing_v2.types.subnets

        out["subnets"] = (
            aws_sdk_elastic_load_balancing_v2.types.subnets.deserialize_query(
                child_subnets
            )
        )
    child_subnet_mappings = el.find("SubnetMappings")
    if child_subnet_mappings is not None:
        import aws_sdk_elastic_load_balancing_v2.types.subnet_mappings

        out["subnet_mappings"] = (
            aws_sdk_elastic_load_balancing_v2.types.subnet_mappings.deserialize_query(
                child_subnet_mappings
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
    child_enable_prefix_for_ipv6_source_nat = el.find("EnablePrefixForIpv6SourceNat")
    if child_enable_prefix_for_ipv6_source_nat is not None:
        import aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum

        out["enable_prefix_for_ipv6_source_nat"] = (
            aws_sdk_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.deserialize_query(
                child_enable_prefix_for_ipv6_source_nat
            )
        )
    return out
