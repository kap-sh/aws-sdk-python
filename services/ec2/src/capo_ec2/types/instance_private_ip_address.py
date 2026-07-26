"""Generated from Smithy shape ``com.amazonaws.ec2#InstancePrivateIpAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_network_interface_association
    import capo_ec2.types.string


class InstancePrivateIpAddress(TypedDict, closed=True):
    association: NotRequired[
        "capo_ec2.types.instance_network_interface_association.InstanceNetworkInterfaceAssociation"
    ]
    """<p>The association information for an Elastic IP address for the network interface.</p>"""
    primary: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this IPv4 address is the primary private IP address of the network interface.</p>"""
    private_dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The private IPv4 DNS name.</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The private IPv4 address of the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstancePrivateIpAddress, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "association" in value:
        import capo_ec2.types.instance_network_interface_association

        capo_ec2.types.instance_network_interface_association.serialize_ec2_query(
            value["association"], pairs, f"{prefix}.Association"
        )
    if "primary" in value:
        pairs.append((f"{prefix}.Primary", "true" if value["primary"] else "false"))
    if "private_dns_name" in value:
        pairs.append((f"{prefix}.PrivateDnsName", str(value["private_dns_name"])))
    if "private_ip_address" in value:
        pairs.append((f"{prefix}.PrivateIpAddress", str(value["private_ip_address"])))


def deserialize_ec2_query(el: Element) -> InstancePrivateIpAddress:
    out: InstancePrivateIpAddress = {}  # type: ignore[typeddict-item]
    child_association = el.find("Association")
    if child_association is not None:
        import capo_ec2.types.instance_network_interface_association

        out["association"] = (
            capo_ec2.types.instance_network_interface_association.deserialize_ec2_query(
                child_association
            )
        )
    child_primary = el.find("Primary")
    if child_primary is not None:
        out["primary"] = (child_primary.text or "").lower() == "true"
    child_private_dns_name = el.find("PrivateDnsName")
    if child_private_dns_name is not None:
        out["private_dns_name"] = str(child_private_dns_name.text or "")
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    return out
