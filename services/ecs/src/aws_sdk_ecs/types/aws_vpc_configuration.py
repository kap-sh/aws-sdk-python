"""Generated from Smithy shape ``com.amazonaws.ecs#AwsVpcConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.assign_public_ip
    import aws_sdk_ecs.types.string_list


class AwsVpcConfiguration(TypedDict):
    subnets: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The IDs of the subnets associated with the task or service. There's a limit of 16 subnets that can be specified.</p> <note> <p>All specified subnets must be from the same VPC.</p> </note>"""
    security_groups: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The IDs of the security groups associated with the task or service. If you don't specify a security group, the default security group for the VPC is used. There's a limit of 5 security groups that can be specified.</p> <note> <p>All specified security groups must be from the same VPC.</p> </note>"""
    assign_public_ip: NotRequired["aws_sdk_ecs.types.assign_public_ip.AssignPublicIp"]
    """<p>Whether the task's elastic network interface receives a public IP address. </p> <p>Consider the following when you set this value:</p> <ul> <li> <p>When you use <code>create-service</code> or <code>update-service</code>, the default is <code>DISABLED</code>. </p> </li> <li> <p>When the service <code>deploymentController</code> is <code>ECS</code>, the value must be <code>DISABLED</code>. </p> </li> </ul>"""
