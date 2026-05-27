"""Generated from Smithy shape ``com.amazonaws.ecs#VpcLatticeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.iam_role_arn
    import aws_sdk_ecs.types.string


class VpcLatticeConfiguration(TypedDict):
    role_arn: "aws_sdk_ecs.types.iam_role_arn.IAMRoleArn"
    """<p>The ARN of the IAM role to associate with this VPC Lattice configuration. This is the Amazon ECS infrastructure IAM role that is used to manage your VPC Lattice infrastructure.</p>"""
    target_group_arn: "aws_sdk_ecs.types.string.String"
    """<p>The full Amazon Resource Name (ARN) of the target group or groups associated with the VPC Lattice configuration that the Amazon ECS tasks will be registered to.</p>"""
    port_name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the port mapping to register in the VPC Lattice target group. This is the name of the <code>portMapping</code> you defined in your task definition.</p>"""
