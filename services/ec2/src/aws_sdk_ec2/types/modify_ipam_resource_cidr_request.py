"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamResourceCidrRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.string


class ModifyIpamResourceCidrRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource you want to modify.</p>"""
    resource_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR of the resource you want to modify.</p>"""
    resource_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the resource you want to modify.</p>"""
    current_ipam_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the current scope that the resource CIDR is in.</p>"""
    destination_ipam_scope_id: NotRequired[
        "aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"
    ]
    """<p>The ID of the scope you want to transfer the resource CIDR to.</p>"""
    monitored: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Determines if the resource is monitored by IPAM. If a resource is monitored, the resource is discovered by IPAM and you can view details about the resource’s CIDR.</p>"""
