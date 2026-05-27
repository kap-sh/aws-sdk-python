"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_id


class DeleteIpamRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM to delete.</p>"""
    cascade: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes. You cannot delete the IPAM with this option if there is a pool in your public scope. If you use this option, IPAM does the following:</p> <ul> <li> <p>Deallocates any CIDRs allocated to VPC resources (such as VPCs) in pools in private scopes.</p> <note> <p>No VPC resources are deleted as a result of enabling this option. The CIDR associated with the resource will no longer be allocated from an IPAM pool, but the CIDR itself will remain unchanged.</p> </note> </li> <li> <p>Deprovisions all IPv4 CIDRs provisioned to IPAM pools in private scopes.</p> </li> <li> <p>Deletes all IPAM pools in private scopes.</p> </li> <li> <p>Deletes all non-default private scopes in the IPAM.</p> </li> <li> <p>Deletes the default public and private scopes and the IPAM.</p> </li> </ul>"""
