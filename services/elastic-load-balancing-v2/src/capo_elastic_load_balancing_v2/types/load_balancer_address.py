"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#LoadBalancerAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.allocation_id
    import capo_elastic_load_balancing_v2.types.i_pv6_address
    import capo_elastic_load_balancing_v2.types.ip_address
    import capo_elastic_load_balancing_v2.types.private_i_pv4_address


class LoadBalancerAddress(TypedDict, closed=True):
    ip_address: NotRequired["capo_elastic_load_balancing_v2.types.ip_address.IpAddress"]
    """<p>The static IP address.</p>"""
    allocation_id: NotRequired[
        "capo_elastic_load_balancing_v2.types.allocation_id.AllocationId"
    ]
    """<p>[Network Load Balancers] The allocation ID of the Elastic IP address for an internal-facing load balancer.</p>"""
    private_i_pv4_address: NotRequired[
        "capo_elastic_load_balancing_v2.types.private_i_pv4_address.PrivateIPv4Address"
    ]
    """<p>[Network Load Balancers] The private IPv4 address for an internal load balancer.</p>"""
    i_pv6_address: NotRequired[
        "capo_elastic_load_balancing_v2.types.i_pv6_address.IPv6Address"
    ]
    """<p>[Network Load Balancers] The IPv6 address.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancerAddress, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ip_address" in value:
        pairs.append((f"{key_prefix}IpAddress", str(value["ip_address"])))
    if "allocation_id" in value:
        pairs.append((f"{key_prefix}AllocationId", str(value["allocation_id"])))
    if "private_i_pv4_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIPv4Address", str(value["private_i_pv4_address"]))
        )
    if "i_pv6_address" in value:
        pairs.append((f"{key_prefix}IPv6Address", str(value["i_pv6_address"])))


def deserialize_query(el: Element) -> LoadBalancerAddress:
    out: LoadBalancerAddress = {}  # type: ignore[typeddict-item]
    child_ip_address = el.find("IpAddress")
    if child_ip_address is not None:
        out["ip_address"] = str(child_ip_address.text or "")
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_private_i_pv4_address = el.find("PrivateIPv4Address")
    if child_private_i_pv4_address is not None:
        out["private_i_pv4_address"] = str(child_private_i_pv4_address.text or "")
    child_i_pv6_address = el.find("IPv6Address")
    if child_i_pv6_address is not None:
        out["i_pv6_address"] = str(child_i_pv6_address.text or "")
    return out
