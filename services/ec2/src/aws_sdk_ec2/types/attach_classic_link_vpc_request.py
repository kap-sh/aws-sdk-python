"""Generated from Smithy shape ``com.amazonaws.ec2#AttachClassicLinkVpcRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.group_id_string_list
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.vpc_id


class AttachClassicLinkVpcRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the EC2-Classic instance.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the ClassicLink-enabled VPC.</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_id_string_list.GroupIdStringList"]
    """<p>The IDs of the security groups. You cannot specify security groups from a different VPC.</p>"""
