"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateSecurityGroupRuleDescriptionsEgressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ip_permission_list
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_name
    import aws_sdk_ec2.types.security_group_rule_description_list


class UpdateSecurityGroupRuleDescriptionsEgressRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.security_group_name.SecurityGroupName"]
    """<p>[Default VPC] The name of the security group. You must specify either the security group ID or the security group name.</p>"""
    ip_permissions: NotRequired["aws_sdk_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The IP permissions for the security group rule. You must specify either the IP permissions or the description.</p>"""
    security_group_rule_descriptions: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_description_list.SecurityGroupRuleDescriptionList"
    ]
    """<p>The description for the egress security group rules. You must specify either the description or the IP permissions.</p>"""
