"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.eip_allocation_public_ip
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.string


class AssociateAddressRequest(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.allocation_id.AllocationId"]
    """<p>The allocation ID. This is required.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance. The instance must have exactly one attached network interface. You can specify either the instance ID or the network interface ID, but not both.</p>"""
    public_ip: NotRequired[
        "aws_sdk_ec2.types.eip_allocation_public_ip.EipAllocationPublicIp"
    ]
    """<p>Deprecated.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface. If the instance has more than one network interface, you must specify a network interface ID.</p> <p>You can specify either the instance ID or the network interface ID, but not both. </p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.</p>"""
    allow_reassociation: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Reassociation is automatic, but you can specify false to ensure the operation fails if the Elastic IP address is already associated with another resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateAddressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allocation_id" in value:
        pairs.append((f"{prefix}.AllocationId", str(value["allocation_id"])))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "public_ip" in value:
        pairs.append((f"{prefix}.PublicIp", str(value["public_ip"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "private_ip_address" in value:
        pairs.append((f"{prefix}.PrivateIpAddress", str(value["private_ip_address"])))
    if "allow_reassociation" in value:
        pairs.append(
            (
                f"{prefix}.AllowReassociation",
                "true" if value["allow_reassociation"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> AssociateAddressRequest:
    out: AssociateAddressRequest = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("AllocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    child_allow_reassociation = el.find("AllowReassociation")
    if child_allow_reassociation is not None:
        out["allow_reassociation"] = (
            child_allow_reassociation.text or ""
        ).lower() == "true"
    return out
