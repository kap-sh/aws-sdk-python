"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class NetworkInterfaceAssociation(TypedDict, closed=True):
    allocation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The allocation ID.</p>"""
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association ID.</p>"""
    ip_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Elastic IP address owner.</p>"""
    public_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public DNS name.</p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The address of the Elastic IP address bound to the network interface.</p>"""
    customer_owned_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customer-owned IP address associated with the network interface.</p>"""
    carrier_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The carrier IP address associated with the network interface.</p> <p>This option is only available when the network interface is in a subnet which is associated with a Wavelength Zone.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInterfaceAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allocation_id" in value:
        pairs.append((f"{prefix}.AllocationId", str(value["allocation_id"])))
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "ip_owner_id" in value:
        pairs.append((f"{prefix}.IpOwnerId", str(value["ip_owner_id"])))
    if "public_dns_name" in value:
        pairs.append((f"{prefix}.PublicDnsName", str(value["public_dns_name"])))
    if "public_ip" in value:
        pairs.append((f"{prefix}.PublicIp", str(value["public_ip"])))
    if "customer_owned_ip" in value:
        pairs.append((f"{prefix}.CustomerOwnedIp", str(value["customer_owned_ip"])))
    if "carrier_ip" in value:
        pairs.append((f"{prefix}.CarrierIp", str(value["carrier_ip"])))


def deserialize_ec2_query(el: Element) -> NetworkInterfaceAssociation:
    out: NetworkInterfaceAssociation = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_ip_owner_id = el.find("IpOwnerId")
    if child_ip_owner_id is not None:
        out["ip_owner_id"] = str(child_ip_owner_id.text or "")
    child_public_dns_name = el.find("PublicDnsName")
    if child_public_dns_name is not None:
        out["public_dns_name"] = str(child_public_dns_name.text or "")
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    child_customer_owned_ip = el.find("CustomerOwnedIp")
    if child_customer_owned_ip is not None:
        out["customer_owned_ip"] = str(child_customer_owned_ip.text or "")
    child_carrier_ip = el.find("CarrierIp")
    if child_carrier_ip is not None:
        out["carrier_ip"] = str(child_carrier_ip.text or "")
    return out
