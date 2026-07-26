"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateAddressResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.domain_type
    import capo_ec2.types.string


class AllocateAddressResult(TypedDict, closed=True):
    allocation_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID that represents the allocation of the Elastic IP address.</p>"""
    public_ipv4_pool: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of an address pool that you own.</p>"""
    network_border_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.</p>"""
    domain: NotRequired["capo_ec2.types.domain_type.DomainType"]
    """<p>The network (<code>vpc</code>).</p>"""
    customer_owned_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>The customer-owned IP address.</p>"""
    customer_owned_ipv4_pool: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the customer-owned address pool.</p>"""
    carrier_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>The carrier IP address. Available only for network interfaces that reside in a subnet in a Wavelength Zone.</p>"""
    public_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon-owned IP address. Not available when using an address pool that you own.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AllocateAddressResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allocation_id" in value:
        pairs.append((f"{prefix}.AllocationId", str(value["allocation_id"])))
    if "public_ipv4_pool" in value:
        pairs.append((f"{prefix}.PublicIpv4Pool", str(value["public_ipv4_pool"])))
    if "network_border_group" in value:
        pairs.append(
            (f"{prefix}.NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "domain" in value:
        import capo_ec2.types.domain_type

        capo_ec2.types.domain_type.serialize_ec2_query(
            value["domain"], pairs, f"{prefix}.Domain"
        )
    if "customer_owned_ip" in value:
        pairs.append((f"{prefix}.CustomerOwnedIp", str(value["customer_owned_ip"])))
    if "customer_owned_ipv4_pool" in value:
        pairs.append(
            (f"{prefix}.CustomerOwnedIpv4Pool", str(value["customer_owned_ipv4_pool"]))
        )
    if "carrier_ip" in value:
        pairs.append((f"{prefix}.CarrierIp", str(value["carrier_ip"])))
    if "public_ip" in value:
        pairs.append((f"{prefix}.PublicIp", str(value["public_ip"])))


def deserialize_ec2_query(el: Element) -> AllocateAddressResult:
    out: AllocateAddressResult = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_public_ipv4_pool = el.find("PublicIpv4Pool")
    if child_public_ipv4_pool is not None:
        out["public_ipv4_pool"] = str(child_public_ipv4_pool.text or "")
    child_network_border_group = el.find("NetworkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    child_domain = el.find("Domain")
    if child_domain is not None:
        import capo_ec2.types.domain_type

        out["domain"] = capo_ec2.types.domain_type.deserialize_ec2_query(child_domain)
    child_customer_owned_ip = el.find("CustomerOwnedIp")
    if child_customer_owned_ip is not None:
        out["customer_owned_ip"] = str(child_customer_owned_ip.text or "")
    child_customer_owned_ipv4_pool = el.find("CustomerOwnedIpv4Pool")
    if child_customer_owned_ipv4_pool is not None:
        out["customer_owned_ipv4_pool"] = str(child_customer_owned_ipv4_pool.text or "")
    child_carrier_ip = el.find("CarrierIp")
    if child_carrier_ip is not None:
        out["carrier_ip"] = str(child_carrier_ip.text or "")
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    return out
