"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterfaceAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceNetworkInterfaceAssociation(TypedDict):
    carrier_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The carrier IP address associated with the network interface.</p>"""
    customer_owned_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer-owned IP address associated with the network interface.</p>"""
    ip_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the owner of the Elastic IP address.</p>"""
    public_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public DNS name.</p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public IP address or Elastic IP address bound to the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceNetworkInterfaceAssociation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "carrier_ip" in value:
        pairs.append((f"{prefix}.CarrierIp", str(value["carrier_ip"])))
    if "customer_owned_ip" in value:
        pairs.append((f"{prefix}.CustomerOwnedIp", str(value["customer_owned_ip"])))
    if "ip_owner_id" in value:
        pairs.append((f"{prefix}.IpOwnerId", str(value["ip_owner_id"])))
    if "public_dns_name" in value:
        pairs.append((f"{prefix}.PublicDnsName", str(value["public_dns_name"])))
    if "public_ip" in value:
        pairs.append((f"{prefix}.PublicIp", str(value["public_ip"])))


def deserialize_ec2_query(el: Element) -> InstanceNetworkInterfaceAssociation:
    out: InstanceNetworkInterfaceAssociation = {}  # type: ignore[typeddict-item]
    child_carrier_ip = el.find("CarrierIp")
    if child_carrier_ip is not None:
        out["carrier_ip"] = str(child_carrier_ip.text or "")
    child_customer_owned_ip = el.find("CustomerOwnedIp")
    if child_customer_owned_ip is not None:
        out["customer_owned_ip"] = str(child_customer_owned_ip.text or "")
    child_ip_owner_id = el.find("IpOwnerId")
    if child_ip_owner_id is not None:
        out["ip_owner_id"] = str(child_ip_owner_id.text or "")
    child_public_dns_name = el.find("PublicDnsName")
    if child_public_dns_name is not None:
        out["public_dns_name"] = str(child_public_dns_name.text or "")
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    return out
