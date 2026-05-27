"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceNetworkAclAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_acl_association_id
    import aws_sdk_ec2.types.network_acl_id


class ReplaceNetworkAclAssociationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    association_id: NotRequired[
        "aws_sdk_ec2.types.network_acl_association_id.NetworkAclAssociationId"
    ]
    """<p>The ID of the current association between the original network ACL and the subnet.</p>"""
    network_acl_id: NotRequired["aws_sdk_ec2.types.network_acl_id.NetworkAclId"]
    """<p>The ID of the new network ACL to associate with the subnet.</p>"""
