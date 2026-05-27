"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
