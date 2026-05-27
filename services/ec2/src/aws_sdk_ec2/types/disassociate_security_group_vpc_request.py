"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateSecurityGroupVpcRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.disassociate_security_group_vpc_security_group_id
    import aws_sdk_ec2.types.string


class DisassociateSecurityGroupVpcRequest(TypedDict):
    group_id: NotRequired[
        "aws_sdk_ec2.types.disassociate_security_group_vpc_security_group_id.DisassociateSecurityGroupVpcSecurityGroupId"
    ]
    """<p>A security group ID.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A VPC ID.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
