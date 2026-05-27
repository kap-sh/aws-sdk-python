"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeSecurityGroupIngressResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ip_permission_list
    import aws_sdk_ec2.types.revoked_security_group_rule_list

RevokeSecurityGroupIngressResult = TypedDict(
    "RevokeSecurityGroupIngressResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
        "unknown_ip_permissions": NotRequired[
            "aws_sdk_ec2.types.ip_permission_list.IpPermissionList"
        ],
        "revoked_security_group_rules": NotRequired[
            "aws_sdk_ec2.types.revoked_security_group_rule_list.RevokedSecurityGroupRuleList"
        ],
    },
)
