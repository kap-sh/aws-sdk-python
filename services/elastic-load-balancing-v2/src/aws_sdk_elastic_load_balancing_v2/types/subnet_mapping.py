"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SubnetMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.allocation_id
    import aws_sdk_elastic_load_balancing_v2.types.i_pv6_address
    import aws_sdk_elastic_load_balancing_v2.types.private_i_pv4_address
    import aws_sdk_elastic_load_balancing_v2.types.source_nat_ipv6_prefix
    import aws_sdk_elastic_load_balancing_v2.types.subnet_id


class SubnetMapping(TypedDict, closed=True):
    subnet_id: NotRequired["aws_sdk_elastic_load_balancing_v2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    allocation_id: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.allocation_id.AllocationId"
    ]
    """<p>[Network Load Balancers] The allocation ID of the Elastic IP address for an internet-facing load balancer.</p>"""
    private_i_pv4_address: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.private_i_pv4_address.PrivateIPv4Address"
    ]
    """<p>[Network Load Balancers] The private IPv4 address for an internal load balancer.</p>"""
    i_pv6_address: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.i_pv6_address.IPv6Address"
    ]
    """<p>[Network Load Balancers] The IPv6 address.</p>"""
    source_nat_ipv6_prefix: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.source_nat_ipv6_prefix.SourceNatIpv6Prefix"
    ]
    """<p>[Network Load Balancers with UDP listeners] The IPv6 prefix to use for source NAT. Specify an IPv6 prefix (/80 netmask) from the subnet CIDR block or <code>auto_assigned</code> to use an IPv6 prefix selected at random from the subnet CIDR block.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SubnetMapping, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "allocation_id" in value:
        pairs.append((f"{prefix}.AllocationId", str(value["allocation_id"])))
    if "private_i_pv4_address" in value:
        pairs.append(
            (f"{prefix}.PrivateIPv4Address", str(value["private_i_pv4_address"]))
        )
    if "i_pv6_address" in value:
        pairs.append((f"{prefix}.IPv6Address", str(value["i_pv6_address"])))
    if "source_nat_ipv6_prefix" in value:
        pairs.append(
            (f"{prefix}.SourceNatIpv6Prefix", str(value["source_nat_ipv6_prefix"]))
        )


def deserialize_query(el: Element) -> SubnetMapping:
    out: SubnetMapping = {}  # type: ignore[typeddict-item]
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_private_i_pv4_address = el.find("PrivateIPv4Address")
    if child_private_i_pv4_address is not None:
        out["private_i_pv4_address"] = str(child_private_i_pv4_address.text or "")
    child_i_pv6_address = el.find("IPv6Address")
    if child_i_pv6_address is not None:
        out["i_pv6_address"] = str(child_i_pv6_address.text or "")
    child_source_nat_ipv6_prefix = el.find("SourceNatIpv6Prefix")
    if child_source_nat_ipv6_prefix is not None:
        out["source_nat_ipv6_prefix"] = str(child_source_nat_ipv6_prefix.text or "")
    return out
