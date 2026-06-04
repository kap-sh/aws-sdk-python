"""Generated from Smithy shape ``com.amazonaws.ecs#VpcLatticeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ecs.errors import DeserializationError

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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcLatticeConfiguration) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["targetGroupArn"] = value["target_group_arn"]
    out["portName"] = value["port_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcLatticeConfiguration:
    out: VpcLatticeConfiguration = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("VpcLatticeConfiguration.role_arn required")
    if "targetGroupArn" in data:
        out["target_group_arn"] = data["targetGroupArn"]
    else:
        raise DeserializationError("VpcLatticeConfiguration.target_group_arn required")
    if "portName" in data:
        out["port_name"] = data["portName"]
    else:
        raise DeserializationError("VpcLatticeConfiguration.port_name required")
    return out
