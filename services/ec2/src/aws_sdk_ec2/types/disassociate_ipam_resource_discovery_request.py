"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateIpamResourceDiscoveryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_resource_discovery_association_id


class DisassociateIpamResourceDiscoveryRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_resource_discovery_association_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_association_id.IpamResourceDiscoveryAssociationId"
    ]
    """<p>A resource discovery association ID.</p>"""
