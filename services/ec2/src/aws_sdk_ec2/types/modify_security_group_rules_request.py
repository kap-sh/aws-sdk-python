"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySecurityGroupRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_rule_update_list


class ModifySecurityGroupRulesRequest(TypedDict):
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    security_group_rules: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_update_list.SecurityGroupRuleUpdateList"
    ]
    """<p>Information about the security group properties to update.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
