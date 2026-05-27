"""Generated from Smithy shape ``com.amazonaws.ec2#RevokedSecurityGroupRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_rule_id
    import aws_sdk_ec2.types.string


class RevokedSecurityGroupRule(TypedDict):
    security_group_rule_id: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_id.SecurityGroupRuleId"
    ]
    """<p>A security group rule ID.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>A security group ID.</p>"""
    is_egress: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Defines if a security group rule is an outbound rule.</p>"""
    ip_protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group rule's protocol.</p>"""
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The 'from' port number of the security group rule.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The 'to' port number of the security group rule.</p>"""
    cidr_ipv4: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR of the traffic source.</p>"""
    cidr_ipv6: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR of the traffic source.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of a prefix list that's the traffic source.</p>"""
    referenced_group_id: NotRequired[
        "aws_sdk_ec2.types.security_group_id.SecurityGroupId"
    ]
    """<p>The ID of a referenced security group.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the revoked security group rule.</p>"""
